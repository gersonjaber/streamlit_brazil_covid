import pandas as pd
import streamlit as st
import altair as alt #https://altair-viz.github.io/

@st.cache(allow_output_mutation=True)
def get_df():
    
    path = f"https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv"
    df = pd.read_csv(path)
    
    return df

def chart(df, y, chart_type):
   
    if chart_type == "bar" :
        return (
            alt.Chart(df, width=750, height=500)
            .mark_bar()
            .encode(
                x="state",
                y=alt.Y(y),
                color="state",
                tooltip=[alt.Tooltip("state"), alt.Tooltip(y)],
            )
            .interactive()
        )
    else :
        return (
            alt.Chart(df, width=750, height=500)
            .mark_point()
            .encode(
                x="state",
                y=alt.Y(y),
                color="state",
                shape="state",
                tooltip=[alt.Tooltip("state"), alt.Tooltip(y)],
            )
            .interactive()
        )

def main():
    
    df = get_df()
    df = df.drop(labels=0, axis=0)
    
    chart_type = st.radio("Choose Chart Type", ["Bar", "Point"])
    chart_type = chart_type.lower()
    
    st.markdown(f"## Confirmed cases 😷")
    st.altair_chart(chart(df, "totalCases", chart_type))
    
    st.markdown(f"## Deaths ")
    st.altair_chart(chart(df, "deaths", chart_type))

    st.markdown("## Vaccinated")
    st.altair_chart(chart(df, "vaccinated", chart_type))

    st.dataframe(df)

if __name__ == "__main__":
    st.title("COVID-19 Brazil 🦠")
    main()