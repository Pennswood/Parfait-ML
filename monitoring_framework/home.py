import streamlit as st

def main():
    st.write("Hello! My name is Normen Yu, a student at Pennsylvania State University. This web application is inspired by my bachelor thesis advisor Dr. Gan Tan and Dr. Saeid Tizpaz-Niari’s research on strategies to mitigate unfairness in machine learning algorithms. As machine learning becomes more prevalent in use for critical social decisions such as court systems, loan approval systems, and predicting income, so too does its potential impact if they are fundamentally unjust or unfair. Hence, fairness in machine learning has become a topic of hot discussion and research. Personally, I believe that bias in machine learning algorithms is fundamentally a human construct, and therefore requires humans to intervene on a case-by-case basis. To do this require in-depth understanding of 1) the trade-offs between and accuracy/efficiency to the general population, 2) thorough understanding of why a model made a specific decision, and 3) the historic nature of bias in pre-existing data. This application provides the framework and a specific proof-of-concept to visualize these complex logic in an intuitive fashion.")
    st.write("This project leverages some industrial tools I have used during my internships (Streamlit, Plotly, etc) to create an application that can help researchers analyze and visualize bias in their learned models. These tools utilized are selected because they require minimum set-up: any developer with Python/pip set-up can easily spin-up my scripts on https://github.com/Pennswood/Parfait-ML/tree/live-streamlit-app, make modifications, and adapt to each researcher’s use case. With just a streamlit command and a python script, there is no heavy back-end set-up to spin up a localhost web-app! Ultimately, the goal of this project is to inspire even those with non-technical background – political scientists, decision makers, social workers, businessman, and so many more with low-to-no understanding of machine learning or statistics – to be able to use this tool and understand intuitively what is happening (the 'means') and what is at stake (the 'ends').")

    dataset = st.file_uploader("Input your dataset here", type=["csv"])
    model = st.file_uploader("Input your model here", type=["pkl"])