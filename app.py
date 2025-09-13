import streamlit as st

def main():
    
    st.markdown("<h1 style='text-align: center;'>1RM Bench Press Calculator</h1>", unsafe_allow_html=True)
    
    unidad = st.selectbox(
        '',
        ['kg', 'lb'])
    
    weight_lifted = st.number_input("Lifted", 20, 10000000000)
    reps = st.number_input("Reps", 1, 10000000000)
    
    def rmcalculator(weight_lifted, reps):
        if reps == 1:
            return weight_lifted
        else:
            return round((weight_lifted * (1 + 0.0333 * reps)), 0)
    
    st.success(f"Your 1RM is: {rmcalculator(weight_lifted, reps)} {unidad}")
    
if __name__ == '__main__':
    main()