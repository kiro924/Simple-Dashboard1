
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide',
                  page_title='simple dashboard'
                  )
df=px.data.tips()

x=st.sidebar.checkbox('show data' , False , key=1)
day=st.sidebar.selectbox('select day' , df['day'].unique())
time=st.sidebar.selectbox('select time' , df['time'].unique())
size=st.sidebar.radio('select how mant dishes' , sorted(df['size'].unique()) , horizontal=True)

if x:
    st.header('dataset sample')
    st.dataframe(df.head(8))

col1 , col2 , col3 =st.columns([5,5,5])

with col1:
    new_def1=df[df['day']==day]
    fig=px.histogram(new_def1  , x='total_bill', color='sex' ,
                     title=f'total bill for {day}'.title())
    st.plotly_chart(fig , use_container_width=True)

    new_def1=df[df['size']==size]
    fig=px.pie(new_def1 , names='time' , color='sex' , 
               title=f'count of each meal time according to {size} dishes'.title()).update_traces(textinfo='value')
    st.plotly_chart(fig , use_container_width=True)

with col3:
    new_def2=df[df['time']==time]
    fig=px.scatter(new_def2 , x='total_bill' , y='tip' , color='sex' ,
                   title=f'correlation between total bill and tip on {time}'.title())
    st.plotly_chart(fig , use_container_width=True)

    fig=px.sunburst(df , path=['day','time'] , color='tip' , 
                    title= 'counting over day, time and size over tips'.title())
    st.plotly_chart(fig)
