#api=cb4c560e8fc89bce06f0393446c
import streamlit as st
import requests
API_key="cb4c560e8fc89bce06f0393446cc04c2"


#

def convert(kx):
    return kx-273.15




def find_weather(city):
    b_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
    weather_data = requests.get(b_url).json()
   # return st.json(weather_data)
    try:
        general = weather_data["weather"][0]["main"]
        icon_id = weather_data["weather"][0]["icon"]
        xtemp   = weather_data['main']['temp']
        temp    = convert(xtemp)
        temprature=round(temp)
        icon=f' https://openweathermap.org/img/wn/{icon_id}@2x.png'
    except keyError:
        st.error('city not found')
        st.stop()
    return general,temprature,icon     




def main():
    st.header("Find Weather")
    city=st.text_input("Enter City Name").lower()
    if st.button('Find'):
        general,temprature,icon=find_weather(city)
        col1,col2=st.columns(2)
        with col1:
            st.metric(label='temp',value=f'{temprature}C')
        with col2:
               st.write(general)
               st.image(icon)

if __name__=='__main__':
    main()