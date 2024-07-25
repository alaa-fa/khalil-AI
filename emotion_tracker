import streamlit as st
import pandas as pd
from textblob import TextBlob
import datetime

import matplotlib.pyplot as plt
from PIL import Image

def main():
    st.set_page_config(layout="wide")
    col1, col2 = st.columns([0.3,0.7])
    with col1:
        MoodyCat=st.empty()
        with MoodyCat.container():
            st.markdown("![Alt Text](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG5pbWxtaWIwNTV5b2V5cXBhN293ZDUyNjFocDRnaTMyOGZtbmk0ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/edru4vHO2OGpTB2htT/giphy.webp)")
    
    if "data" not in st.session_state:
        st.session_state.data = []
        st.session_state.static_data_added = False
    with col2:
        st.title("Mood Journal")
    


        text_input = st.text_area("How do you feel today?")

        if st.button("Submit"):
            if text_input:
                analysis = TextBlob(text_input)
                sentiment = analysis.sentiment.polarity

                if sentiment > 0:
                    mood = "Positive"
                    with col1:
                        MoodyCat.empty()
                        with MoodyCat.container():
                            st.markdown("![Alt Text](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3BtYXQxaWVuaGd6b3QweGhpdjdsZ3E5N2tiMzVzNno4a2M0ZjhpZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ogJaybCTlxckYOoDYq/giphy.webp)")
    
                elif sentiment < 0:
                    mood = "Negative"
                    with col1:
                        MoodyCat.empty()
                        with MoodyCat.container():
                            st.markdown("![Alt Text](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDcwY29ld3I3ZmV1MHgzdDY2Mnlnb3BkaTdnd2Vybm53Y25zZmQ3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jnD6cZTCrNBkIAqSTN/giphy.webp)")
                      

                        # Emojis
                        sad_emoji = "😔"
                        chatbot_icon = "💬"
                        games_icon = "🎮"
                        videos_icon = "🎥"
                        yoga_icon = "🧘‍♀️"

                        # Title
                        st.title("We're Here to Help")

                        # Main message with emoji
                        st.write(f"{sad_emoji} It seems like you're feeling down. If you want to talk, 'Khalil' is ready to chat with you.")

                        # Games section with emoji
                        st.header(f"{games_icon} Love to play games?")
                        st.write("- Poki: https://www.poki.com")
                        st.write("- CrazyGames: https://www.crazygames.com")
                        st.write("- Armor Games: https://www.armorgames.com")
                        st.write("- Steam: https://store.steampowered.com/")

                        # Videos section with emoji
                        st.header(f"{videos_icon} Enjoy watching videos?")
                        st.write("- Tashima: https://youtube.com/@tashmeera?si=pE-Wp5FWyIix1evY")
                        st.write("- Areeca: https://youtube.com/@areekapodcast?si=wjburFydgHXbRDvh")

                        # Yoga section with emoji
                        st.header(f"{yoga_icon} Like sports?")
                        st.write("We recommend yoga. Here are some tutorials:")
                        st.write("- Yoga with Adriene: https://www.youtube.com/user/yogawithadriene")
                        st.write("- Yoga with Tim: https://www.youtube.com/user/vancouveryoga")

                else:
                    mood = "Neutral"

                confidence = abs(sentiment)

                # Get current date without time
                date = datetime.datetime.now().date().strftime('%d-%B-%Y') # Format as day-month-year

                st.session_state.data.append({'Text': text_input, 'Sentiment': mood, 'Confidence': confidence, 'Date': date})

           # Add static data only once
        if not st.session_state.static_data_added:
            yesterday = (datetime.date.today() - datetime.timedelta(days=1))
            static_data = [
                {'Text': 'The stock market is experiencing a downturn.', 'Sentiment': 'Negative', 'Confidence': 0.3, 'Date': (yesterday - datetime.timedelta(days=4)).strftime('%d-%B-%Y')},
                {'Text': 'I am eating an apple.', 'Sentiment': 'Neutral', 'Confidence': 0.7, 'Date': (yesterday - datetime.timedelta(days=3)).strftime('%d-%B-%Y')},
                {'Text': 'I am disappointed with the results.', 'Sentiment': 'Negative', 'Confidence': 0.1, 'Date': (yesterday - datetime.timedelta(days=2)).strftime('%d-%B-%Y')},
                {'Text': 'I don\'t know', 'Sentiment': 'Neutral', 'Confidence': 0.2, 'Date': (yesterday - datetime.timedelta(days=1)).strftime('%d-%B-%Y')},
                {'Text': 'I am excited about the upcoming vacation.', 'Sentiment': 'Positive', 'Confidence': 0.8, 'Date': yesterday.strftime('%d-%B-%Y')},
                # ... more static data points
            ]
            st.session_state.data.extend(static_data)
            st.session_state.static_data_added = True

    
        df = pd.DataFrame(st.session_state.data)
        
        st.dataframe(
    df,
    column_config={
        "Text": st.column_config.TextColumn(width="large"),
        "Sentiment": st.column_config.NumberColumn(width="medium"),
    },
)
        # Plotting (assuming 'Date' is a string now)
        
        # st.line_chart(
        #     df,
        #     x='Date',
        #     y='Sentiment',
        #     # You can add color here if needed
        # )
        # st.line_chart(
        #   df, x="Date", y=["Confidence", "Sentiment"], color=["#FF0000", "#0000FF"]  # Optional
        # )
        # Pivot the DataFrame to get the desired format for plotting
        # df_pivot = df.pivot_table(index='Date', columns='Sentiment', values='Confidence')

        # # Create the line chart
        # st.line_chart(df_pivot)
        # Count occurrences of each sentiment per day
       

        # Pivot the data to have Sentiment as columns and Count as values
        df_pivot = df.pivot_table(index='Date', columns='Sentiment', values='Confidence', fill_value=0)

        # Create the line chart
        st.line_chart(df_pivot)

if __name__ == "__main__":
    main()
