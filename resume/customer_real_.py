import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

loadmodel=pickle.load(open('customermodel.sav','rb'))
loadthemodel=pickle.load(open('scaledSVMmodel_.sav','rb'))
RFmodel=pickle.load(open('trained_model_.sav','rb'))
Logmodel=pickle.load(open('logisticmodel.sav','rb'))

df=pd.read_csv('Customer_Behaviour.csv')

rad=st.sidebar.radio("Navigation",["Description","Prediction Model","Data Visualization"])

if rad=="Data Visualization":
    st.title("Countplot of Gender with respect to Purchased")
    sns.countplot(data=df,x='Gender',hue='Purchased')
    plt.show()
    st.pyplot(fig=None)

    st.title("Displot Age")
    sns.displot(data=df,x='Age')
    plt.show()
    st.pyplot(fig=None)
    
    st.title("Pair Plot")
    sns.pairplot(df)
    plt.show()
    st.pyplot(fig=None)

if rad=="Description":
    st.title(":blue[Customer Behaviour Analysis]")
    st.video("customer.mp4")
    st.header(":blue[Objective]")
    st.markdown("""
    
    ###### If any company or show-room manager have to find out whether their old or new customer want to buy there product how can they find out that. This can be achieved if they have data about customer salary age and other factor field(independent variables) to find out if customer will purchased(dependent variable). \n
    In this project, we will try to predict if the customer purchase the product or not using various machine learning models
    """)

    st.markdown("""
    #### :blue[Dataset Description]
    :blue[Gender] :  Male or Female\n
    :blue[Age] :  Customer Age\n
    :blue[Estimated Salary]\n
    :blue[Purchased] : Whether the customer will make the purchase based on above parameters

    """)

    st.table(df.head())
    st.markdown("""
    #### Click the link to download the dataset.
    """)
    st.download_button(
        label="Download data as CSV",
        data="Customer_Behaviour.csv",
        file_name='Customer_Behaviour.csv',
        mime='text/csv')

if rad=="Prediction Model":
    side=st.selectbox("Choose the model",['SVM','Random Forest'],index=1)
    if side=="SVM":
        def scalar(values):

            values=loadthemodel.transform(values)
            return values

        def SVMmodel(scaled):
            scaled_numpy_array=np.asarray(scaled)
            scaled_reshaped=scaled_numpy_array.reshape(1,-1)
            x=scalar(scaled_reshaped)
            print(x)

            prediction=loadmodel.predict(x)
            print(prediction)

            if prediction==0:
                return "Not purchased"
            elif prediction==1:
                 return "Purchased"

        def main():
            st.title("SVM prediction model")
            gender=st.selectbox("Gender",["Male","Female"],index=1)
            if gender == "Male":
                gender=0
            else:
                gender=1
                st.write(gender)

            age=st.number_input("Age")
            st.write(age)

            salary=st.number_input("Estimated Salary")
            st.write(salary)

            SVM_result=''

            if st.button("Get prediction"):
                SVM_result=SVMmodel([gender,age,salary])

            st.success(SVM_result)

        if __name__=='__main__':
            main()

    if side=="Random Forest":
        def scalar(value):
            input_data_as_numpy_array=np.asarray(value)
            input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

            value=loadthemodel.transform(input_data_reshaped)
            return value

        def RandomModel(scaled):
            scaled_numpy_array=np.asarray(scaled)
            scaled_reshaped=scaled_numpy_array.reshape(1,-1)
            x=scalar(scaled_reshaped)

            prediction=RFmodel.predict(x)
            print(prediction)

            if prediction==0:
                return "Not purchased"
            elif prediction==1:
                 return "Purchased"

        def main():
            st.title("Random Forest prediction model")
            gender=st.selectbox("Gender",['Male','Female'],index=1)
            if gender == 'Male':
                gender=0
            else:
                gender=1
            st.write(gender)

            age=st.number_input("Age")
            st.write(age)

            salary=st.number_input("Estimated Salary")
            st.write(salary)

            RFM_result=''

            if st.button("Get prediction"):
                RFM_result=RandomModel([gender,age,salary])

            st.success(RFM_result)

        if __name__=='__main__':
            main()

