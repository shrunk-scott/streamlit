import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Line
from streamlit_echarts import st_echarts

# Function to create a line chart using Echarts
def line_chart():
    line = (
        Line()
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
        .add_yaxis("Series 1", [1, 2, 3, 4, 5, 6])
        .add_yaxis("Series 2", [6, 5, 4, 3, 2, 1])
        .set_global_opts(title_opts=opts.TitleOpts(title="Chart_name"))
    )
    return line

# Layout of the Streamlit app based on the mockup
def main():
    st.sidebar.image("path_to_logo.png", use_column_width=True)
    st.sidebar.button("Page 1")
    st.sidebar.button("Page 2")
    st.sidebar.button("Page 3")
    
    st.sidebar.checkbox("Checkbox 01")
    st.sidebar.checkbox("Checkbox 02")
    combo_box_options = ["Option 1", "Option 2", "Option 3"]
    st.sidebar.selectbox("ComboBox", combo_box_options)

    st.title("My_app_name")

    # Main content text placeholder
    st.text("This is a placeholder for the main content.")

    # Echarts line chart
    chart = line_chart()
    st_echarts(options=chart.dump_options(), height="400px")

    # Button to download chart data (functionality to be implemented)
    if st.button("Download Chart data"):
        st.write("Chart data will be downloaded (functionality to be added).")

if __name__ == "__main__":
    main()
