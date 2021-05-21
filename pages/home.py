import streamlit as st
def home_elements():
    st.title('COVID -19 Dashboard')
    st.write(
                """
                This web application will serve to analyze,visualize, the spread of the
                novel Coronavirus - 2019 (COVID - 19) caused by acute respiratory syndrome
                coronavirus 2 (SARS-COV-2). It was first identified in 2019 and has resulted
                in ongoing pandemic.
                """
            )
    st.markdown("## Symptoms")
    st.markdown(("* Fever or chills\n* Cough\n"
                    "* Shortness of breath or difficulty breathing\n"
                    "* Fatigue\n"
                    "* Muscle or body aches\n"
                    "* Headache\n"
                    "* Loss of taste or smell\n"
                    "* Sore throat\n"
                    "* Congestion or runny nose\n"
                    "* Nausea or vomiting\n"
                    "* Diarrhea"))
    st.markdown("## To prevent the spread of COVID-19:")
    st.markdown(("* Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n"
                            "* Maintain a safe distance from anyone who is coughing or sneezing.\n"
                            "* Wear a mask when physical distancing is not possible.\n"
                            "* Don’t touch your eyes, nose or mouth.\n"
                            "* Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
                            "* Stay home if you feel unwell.\n"
                            "* If you have a fever, cough and difficulty breathing, seek medical attention.\n"
                        ))