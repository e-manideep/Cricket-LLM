import streamlit as st
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAEnHVjbcA7-jrIhtPJULoBe7sIYBhzsYg"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

def get_response(question):
    """Get the model response for a given question."""
    prompt = (
    f"Please analyze the following question and respond accordingly:\n\n"
    f"1. If the question is asking for IPL data beyond the year 2024, respond with: "
    f"'Sorry, I don't have data beyond 2024. We are working on it. We'll update it soon :)'\n"
    f"2. If the question is asking for cricket data but is not related to IPL for data greater than 2022, respond with: "
    f"'The question is not related to IPL. Please ask a question related to IPL as it is greater than 2022 :)'\n"
    f"3. Otherwise, provide an accurate and informative response to the IPL-related question.\n\n"
    f"Here are some sample questions and their answers to guide you:\n"
    f"1. 'What are the top IPL teams as of 2024?' - Answer: 'As of 2024, the top IPL teams are Mumbai Indians, Chennai Super Kings, Kolkata Knight Riders, Delhi Capitals, and Royal Challengers Bangalore.'\n"
    f"2. 'Who scored the most runs in IPL 2024?' - Answer: 'The highest run-scorer in IPL 2024 was Faf du Plessis with 780 runs.'\n"
    f"3. 'Which team won the IPL 2024?' - Answer: 'The IPL 2024 was won by Chennai Super Kings.'\n"
    f"4. 'What is the highest score by an individual in an IPL match in 2024?' - Answer: 'The highest individual score in an IPL match in 2024 was 135* by Ruturaj Gaikwad.'\n"
    f"5. 'Can you provide the IPL statistics for the top 5 players in 2024?' - Answer: 'The top 5 IPL players in 2024 are: 1. Faf du Plessis, 2. Ruturaj Gaikwad, 3. Virat Kohli, 4. Jos Buttler, 5. Suryakumar Yadav.'\n"
    f"6. 'Who won the match between Delhi Capitals and Chennai Super Kings on March 31, 2024?' - Answer: 'Delhi Capitals won the match against Chennai Super Kings on March 31, 2024 by 20 runs.'\n"
    f"7. 'Which player scored the fastest century in IPL 2024?' - Answer: 'The data provided doesn’t include information about individual batting performances or centuries, so this can’t be determined from the given information.'\n"
    f"8. 'How many matches did Sunrisers Hyderabad play before reaching the final?' - Answer: 'To determine this, we would need to count all matches involving Sunrisers Hyderabad before the final. This requires a detailed analysis of the data.'\n"
    f"9. 'Which team had the most last-over finishes in IPL 2024?' - Answer: 'The data doesn’t provide information about when matches ended, so it’s not possible to determine which team had the most last-over finishes.'\n"
    f"10. 'Who was the player of the match in the first game of IPL 2024?' - Answer: 'Mustafizur Rahman was the player of the match in the first game of IPL 2024.'\n"
    f"11. 'How many matches were played at the Narendra Modi Stadium in Ahmedabad during IPL 2024?' - Answer: 'To determine this, we would need to count all matches listed as being played at Narendra Modi Stadium, Ahmedabad. This requires a detailed count through the data.'\n"
    f"12. 'Which team won the most matches while chasing in IPL 2024?' - Answer: 'To answer this, we would need to analyze each match result and count wins for teams batting second. This requires a comprehensive analysis of the data.'\n"
    f"13. 'What was the result of the match between Mumbai Indians and Royal Challengers Bengaluru on April 11, 2024?' - Answer: 'Mumbai Indians won the match against Royal Challengers Bengaluru on April 11, 2024 by 7 wickets.'\n"
    f"14. 'How many times did a team score over 200 runs in IPL 2024?' - Answer: 'To determine this, we would need to count all instances where a team’s score exceeded 200. This requires a detailed analysis of the data.'\n"
    f"15. 'Which player won the most “Player of the Match” awards in IPL 2024?' - Answer: 'To answer this, we would need to count the number of times each player is listed in the “player_of_match” column. This requires a comprehensive analysis of the data.'\n"
    f"16. 'What was the lowest successful run chase in IPL 2024?' - Answer: 'Based on the data, the lowest successful chase was 90 runs by Delhi Capitals against Gujarat Titans on April 17, 2024.'\n"
    f"17. 'How many matches did Lucknow Super Giants win in IPL 2024?' - Answer: 'To determine this, we would need to count all matches where Lucknow Super Giants are listed as the winner. This requires a detailed count through the data.'\n"
    f"18. 'Which match had the highest number of sixes hit?' - Answer: 'The data doesn’t provide information about the number of sixes hit in each match, so this can’t be determined from the given information.'\n"
    f"19. 'Who were the umpires for the first match of IPL 2024?' - Answer: 'HAS Khalid and VK Sharma were the umpires for the first match of IPL 2024.'\n"
    f"20. 'What was the result of the last league match before the playoffs in IPL 2024?' - Answer: 'The last league match before the playoffs was between Royal Challengers Bengaluru and Chennai Super Kings on May 18, 2024, which Royal Challengers Bengaluru won by 27 runs.'\n"
    f"21. 'When did IPL 2024 start?' - Answer: 'IPL 2024 started on March 22, 2024, with a match between Royal Challengers Bengaluru and Chennai Super Kings.'\n"
    f"22. 'Which team scored the lowest total in IPL 2024?' - Answer: 'Based on the data provided, the lowest total was 90 runs scored by Gujarat Titans against Delhi Capitals on April 17, 2024.'\n"
    f"23. 'How many matches went to the last over in IPL 2024?' - Answer: 'The data doesn’t provide information about which matches went to the last over, so this can’t be determined from the given information.'\n"
    f"24. 'Which player took the most wickets in a single match in IPL 2024?' - Answer: 'The data doesn’t provide individual bowling performances, so this information can’t be determined from the given data.'\n"
    f"25. 'How many matches did Chennai Super Kings play at their home ground in IPL 2024?' - Answer: 'To determine this, we would need to count the matches played at MA Chidambaram Stadium, Chepauk, Chennai where Chennai Super Kings were one of the teams.'\n"
    f"26. 'Which team had the longest winning streak in IPL 2024?' - Answer: 'To determine this, we would need to analyze the sequence of results for each team, which would require a more detailed analysis of the data.'\n"
    f"27. 'How many times did a team successfully defend a total in IPL 2024?' - Answer: 'To answer this, we would need to count the number of times the team batting first won the match. This would require a detailed count through the data.'\n"
    f"28. 'Which venue hosted the first match of IPL 2024?' - Answer: 'The first match of IPL 2024 was hosted at MA Chidambaram Stadium, Chepauk, Chennai.'\n"
    f"29. 'How many matches in IPL 2024 were affected by DLS method?' - Answer: 'Based on the data, only one match (the final) shows “D/L” in the DLS column, indicating it was affected by the DLS method.'\n"
    f"30. 'Which team won the most tosses in IPL 2024?' - Answer: 'The data doesn’t provide information about who won the toss in each match, so this can’t be determined from the given information.'\n"
    f"31. 'How many different venues were used in IPL 2024?' - Answer: 'To determine this, we would need to count the unique stadiums listed in the data. This would require a detailed analysis.'\n"
    f"32. 'Which match had the smallest margin of victory in IPL 2024?' - Answer: 'The match with the smallest margin of victory was between Kolkata Knight Riders and Lucknow Super Giants on April 14, 2024, where Kolkata won by 1 run.'\n"
    f"33. 'How many matches did Royal Challengers Bengaluru play in IPL 2024?' - Answer: 'To determine this, we would need to count all matches where Royal Challengers Bengaluru is listed as one of the teams. This requires a detailed count through the data.'\n"
    f"34. 'Which team scored the most runs in a single innings while batting second?' - Answer: 'Based on the data, Punjab Kings scored 262 runs while chasing against Kolkata Knight Riders on April 26, 2024, which appears to be the highest second innings score.'\n"
    f"35. 'How many matches in IPL 2024 were won by the team batting first?' - Answer: 'To determine this, we would need to count all matches where the team listed first in the “winner” column matches the team that batted first. This requires a detailed analysis of the data.'\n"
    f"36. 'Who won the IPL 2024 final?' - Answer: 'Kolkata Knight Riders won the IPL 2024 final against Sunrisers Hyderabad by 8 wickets.'\n"
    f"37. 'Where was the IPL 2024 final played?' - Answer: 'The IPL 2024 final was played at MA Chidambaram Stadium, Chepauk, Chennai.'\n"
    f"38. 'Who was the player of the match in the IPL 2024 final?' - Answer: 'MA Starc was the player of the match in the IPL 2024 final.'\n"
    f"39. 'What was the highest team score in IPL 2024?' - Answer: 'The highest team score in IPL 2024 was 262 runs by Punjab Kings against Kolkata Knight Riders on April 26, 2024.'\n\n"
    f"Question: {question}"
)

    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Cricket Q&A", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Q&A Application")
question = st.text_input("Please ask a question related to Cricket:")
if st.button("Get Answer"):
    if question:
        response_text = get_response("Check 2 conditions before response first check if the question asking data greater than 2023 give response sorry i dont have data we are working on it and if the data is not related to cricket give response that please ask the question related to cricket after checking conditions answer the questions"+question)
        st.write(response_text)
    else:
        st.error("Please enter a question.")
st.sidebar.title("About This Project")
st.sidebar.write(
"Overview: The Cricket Q&A Application is an interactive web application designed to answer users questions related to cricket. Built using Streamlit and powered by GG AI model, this application provides accurate and informative responses to cricket-related queries. The application ensures user queries are properly addressed by implementing checks for data relevance and timeframe.Features")
st.sidebar.write("Project developed by **Manideep**, **Koushik**, **Vignesh**, **Kinnera**, **Sunidhi**, and **Sathvika**. Guided by **Mr. B Kiran Kumar**")
