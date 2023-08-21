import streamlit as st
from datetime import datetime, timedelta
import pickle


def main():
    st.title(":violet[Flight Price Prediction]")

    airline = st.sidebar.selectbox(':orange[Airline]',
                                   [None, 'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'])
    airline_dict = {'AirAsia': 0, "Indigo": 1, "GO_FIRST": 2, "SpiceJet": 3, "Air_India": 4, "Vistara": 5}

    source_city = st.sidebar.selectbox(':orange[Source City]',
                                       [None, 'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
    source_dict = {'Delhi': 0, "Hyderabad": 1, "Bangalore": 2, "Mumbai": 3, "Kolkata": 4, "Chennai": 5}

    departure_time = st.sidebar.selectbox(':orange[Departure_Time]',
                                          [None, 'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
                                           'Late_Night'])
    departure_dict = {'Early_Morning': 0, "Morning": 1, "Afternoon": 2, "Evening": 3, "Night": 4, "Late_Night": 5}

    stops = st.sidebar.selectbox(":orange[Stops]", [None, 'zero', 'one', 'two_or_more'])
    stops_dict = {'zero': 0, "one": 1, "two_or_more": 2}

    arrival_time = st.sidebar.selectbox(":orange[Arrival_Time]",
                                        [None, 'Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening',
                                         'Late_Night'])
    arrival_dict = {'Early_Morning': 0, "Morning": 1, "Afternoon": 2, "Evening": 3, "Night": 4, "Late_Night": 5}

    destination_city = st.sidebar.selectbox(':orange[Destination_City]',
                                            [None, 'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
    destination_dict = {'Delhi': 0, "Hyderabad": 1, "Mumbai": 2, "Bangalore": 3, "Chennai": 4, "Kolkata": 5}

    Class = st.sidebar.selectbox(":orange[Class]", [None, 'Economy', 'Business'])
    class_dict = {'Economy': 0, 'Business': 1}

    departure_date = st.sidebar.date_input('Select the departure date', min_value=datetime.today(),
                                           max_value=datetime.today() + timedelta(50))
    date_diff = datetime.strptime(str(departure_date), '%Y-%m-%d') - datetime.today()
    date_diff = int(date_diff.days + 1)

    data = [airline, source_city, departure_time, stops, arrival_time, destination_city, Class, date_diff]

    if None not in data and st.button(':orange[predict]'):
        features = [airline_dict[airline], source_dict[source_city], departure_dict[departure_time], stops_dict[stops],
                    arrival_dict[arrival_time], destination_dict[destination_city], class_dict[Class], date_diff]

        model = pickle.load(open('linear_model.pkl', 'rb'))
        predict = model.predict([features])[0]
        st.subheader(f'Your Flight Price Rs :green[{predict:.2f}]')


if __name__ == "__main__":
    main()
