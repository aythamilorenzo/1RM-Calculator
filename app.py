import streamlit as st



st.set_page_config(page_title = '1RM Bench Press Calculator', page_icon = "🏋️‍♂️")

def main():
    
    st.markdown("<h1 style='text-align: center;'>1RM Bench Press Calculator</h1>", unsafe_allow_html=True)
    
    unit = st.radio('Unit', ['kg', 'lb'])
    
    weight_lifted = st.number_input("Lifted", 20, 10000000000)
    reps = st.number_input("Reps", 1, 10000000000)
    
    def rmcalculator(weight_lifted, reps):
        if reps == 1:
            return weight_lifted
        else:
            return round((weight_lifted * (1 + 0.0333 * reps)), 0)
    
    st.success(f"Your 1RM is approximately: {rmcalculator(weight_lifted, reps)} {unit}")
    
    with st.expander('How do we calculate your 1RM?'):
        st.write("""Our calculations are based on the Epley´s formula which states:
                 
                 1RM = weight_lifted * (1 + 0.0333 * reps)
                 """)
        
        st.write("The coefficient 0.0333 estimates the 1RM taking into account the number of repetitions.")

    

if __name__ == '__main__':
    main()