import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

log_file = "session_log.csv"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if not os.path.isfile(log_file):
    with open(log_file, "w") as f:
        f.write("timestamp,event\n")


if 'log_df' not in st.session_state:
    try:
        st.session_state['log_df'] = pd.read_csv(log_file)
    except:
        st.session_state['log_df'] = pd.DataFrame(columns = ["timestamp", "event"])

st.title("Drowsiness Detection Dashboard")

total_events = len(st.session_state['log_df'])
drowsy_starts = st.session_state['log_df']['event'].value_counts().get('Drowsiness Starts', 0)
st.metric("Drowsy Events", drowsy_starts)

if total_events > 0:
    st.write('### Drowsy Event Log')
    st.dataframe(st.session_state['log_df'])

    
    times = pd.to_datetime(st.session_state['log_df']['timestamp'])
    starts = pd.to_datetime(st.session_state['log_df'][st.session_state['log_df']['event'] == 'Drowsiness Starts']['timestamp'].reset_index(drop=True))
    ends = pd.to_datetime(st.session_state['log_df'][st.session_state['log_df']['event'] == 'Drowsiness Ends']['timestamp'].reset_index(drop=True))


    st.session_state['log_df']['timestamp'] = pd.to_datetime(st.session_state['log_df']['timestamp'])

    if len(starts) >= 2:
        avg_time_between = starts.diff().dropna().mean().total_seconds()
    else:
        avg_time_between = 0

    st.metric("Avg Time Between Drowsy Events (s)", round(avg_time_between, 2))


    if len(starts) == len(ends):
        durations = (ends - starts).dt.total_seconds()
        avg_duration = durations.mean()
    else:
        avg_duration = 0

    st.metric("Avg Drowsy Duration (s)", round(avg_duration, 2))

    fig, ax = plt.subplots()
    drowsy_freq = times.value_counts().sort_index()
    drowsy_freq.plot(ax=ax, marker='o', linestyle='-', title="Drowsiness Frequency Over Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Frequency")
    plt.xticks(rotation=45)
    st.pyplot(fig)

else:
    st.info("No events recorded yet!")
