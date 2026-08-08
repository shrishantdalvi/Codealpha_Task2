import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np 
import joblib
df = pd.read_csv("data/Advertising.csv")
#number of Records and columns
print(df.shape)
#prints the column names
print(df.columns)
#datatype of each columns
print(df.dtypes)
#pritns the row index
print(df.index)
#prints the short information
df.info()
#shows numerical statistics
print(df.describe())
#gives first 5 entries from the all columns
t = df["TV"] #for particular cloumns
print(t.head())
print(df.head())
#gives last 5 entries from all columns
print(df.tail())

# data cleaning
#removing extra spaces from columns name from start and end not the middle
df.columns =df.columns.str.strip()
print(df.columns)
#showing the null values count
print(df.isnull().sum())
#showing the dupicate values count
print(df.duplicated().sum()) 
#checking any negative values
print((df[["TV","Radio","Newspaper"]] < 0).sum())

#Exploratory data analysis
#Histogram of TV  records distribution
plt.hist(df["TV"],bins=12,
         color="#4C78A8",
         edgecolor="#263238",
         linewidth=1.2)
plt.title("Distribution of TV Advertising",fontsize=16,fontweight="bold")
plt.xlabel("TV investments rates",fontsize=12,fontweight="bold")
plt.ylabel("record distribution",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show()  
#histogram of radio records distribution
plt.figure(figsize=(8,5))
plt.hist(df["Radio"],bins=10,
         color="#6A994E",
         edgecolor="#283618",
         linewidth=1.2)
plt.title("Distribution of Radio Advertising",fontsize=16,fontweight="bold")
plt.xlabel("Radio investments rates",fontsize=12,fontweight="bold")
plt.ylabel("record distribution",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show() 
#histogram of Newspaper records of distribution
plt.figure(figsize=(8,5))
plt.hist(df["Newspaper"],bins=10,
         color="#6A4C93",
         edgecolor="#252525",
         linewidth=1.2)
plt.title("Distribution of Newspaper Advertising",fontsize=16,fontweight="bold")
plt.xlabel("Newspaper investments rates",fontsize=12,fontweight="bold")
plt.ylabel("record distribution",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show() 
#scatter plot of TV vs sales
plt.figure(figsize=(8,5))
plt.scatter(df["TV"],
            df["Sales"],
            marker="o",
            color="#7B2CBF",
            edgecolor="#252525",
            linewidth=1.2,
            s=70,
            alpha=0.75)
plt.title("Relation between sales and TV advertisement",fontsize=16,fontweight="bold")
plt.xlabel("TV investments rates",fontsize=12,fontweight="bold")
plt.ylabel("sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show()  
#scatter plot of Radio vs sales
plt.figure(figsize=(8,5))
plt.scatter(df["Radio"],
            df["Sales"],
            marker="o",
            color="#2C82BF",
            edgecolor="#252525",
            linewidth=1.2,
            s=70,
            alpha=0.75)
plt.title("relation between sales and Radio advertisement",fontsize=16,fontweight="bold")
plt.xlabel("Radio investments rates",fontsize=12,fontweight="bold")
plt.ylabel("sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show() 

#scatter polot for sales vs Newspaper
plt.figure(figsize=(8,5))
plt.scatter(df["Newspaper"],
            df["Sales"],
            marker="o",
            color="#F28E2B",
            edgecolor="#252525",
            linewidth=1.2,
            s=70,
            alpha=0.75)
plt.title("relation between sales and Newspaper advertisement",fontsize=16,fontweight="bold")
plt.xlabel("Newspaper investments rates",fontsize=12,fontweight="bold")
plt.ylabel("sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.show()  

#Heatmap for all numerical columns form our dataset
correlation=df[
    [
        "TV",
        "Radio",
        "Newspaper",
        "Sales"
    ]
].corr()
plt.figure(figsize=(8,5))
sns.heatmap(correlation,
            annot=True,
            cmap="RdBu_r",
            fmt=".2f",
            linecolor="White",
            linewidths=3,
            center=0,
            cbar_kws={"label":"correlation"})
plt.title("correlation between all numerical columns by hetmap",fontsize=16,fontweight="bold")
plt.tight_layout()
plt.show()  

#Boxplot for sales
plt.figure(figsize=(6,5))
plt.boxplot(df["Sales"],
            patch_artist=True,
            boxprops=dict(facecolor="#4C78A8", color="#2F2F2F",linewidth=2),
            medianprops=dict(color="#D62728",linewidth=2),
            whiskerprops=dict(color="#2F2F2F",linewidth=1.2),
            capprops=dict(color="#2F2F2F",linewidth=1.2),
            flierprops=dict(marker="o",markerfacecolor="skyblue",markersize=3),
            )
plt.title("sales distribution of records",fontsize=16,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.tight_layout()
plt.show()  

#Machine learning 
df.drop(columns=["Unnamed: 0"],inplace=True)
#Seperate features(x) and target(y)
#features
X = df[["TV","Radio","Newspaper"]] #double [[]] for selecting multiple columns,X uppercase for storing multiple features
#Target
y = df[["Sales"]] #y lowercase basic convention for single column
print(X.head)
print(y.head)
#To make sure target column not the part of feature
X = df.drop("Sales",axis=1)
#train-test_split 
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,                 #spliting data into train:test-->80:20
    random_state=42                #lock the shuffle in same  pattern 42
)
# creating a empty LinearRegression() model
model = LinearRegression()
model.fit(X_train,y_train)       #(this line train the model variable through x_train,y_train which consist the featureinputs
                                    #to predict sales only on the training data) 
y_pred = model.predict(X_test)   # used to store the predicted values by x_test in variable y_pred predict through .predict()

mae = mean_absolute_error(y_test,y_pred)  #compares y_test & y_train and gives the on average at what difference the model predict sales
print("MAE = ",mae)
mse = mean_squared_error(y_test,y_pred)
print("MSE = ",mse)                     #mse gives the average squarred error that is it our model making any large mistakes by squaring the error

rmse = np.sqrt(mean_squared_error(y_test,y_pred))  #it gives on average how much predicted sales units away from actual sales
print("RMSE = ",rmse) 

r2 = r2_score(y_test,y_pred)    #it is model for predicting how much the model showing variations also how much percentage of the  
print("R2: ",r2)                 #columns in the dataset is reasnable for predicting result rest of other then columns in the table

print("Intercept :",model.intercept_)  #.intercept returns the impact on sales when all features at starting point

coefficients = pd.DataFrame({
    "Feature" : X.columns,
    "Coefficient" : model.coef_.flatten()    #.flatten converts a  multidimensional array into 1D
})
print(coefficients)   #returns the each feature contibution in sale when each feature is increased by 1 unit
print(model.coef_.shape)

#Residual plot
residual = y_test - y_pred   #this is to check any kind of error is missing by our model or how good our regression model is working
plt.figure(figsize=(8,5))
plt.scatter(y_pred,residual)
plt.axhline(y=0,color="red",linestyle="--")

plt.title("Residual Plot",fontsize=16,fontweight="bold")
plt.xlabel("Predicted sales",fontsize=12,fontweight="bold")
plt.ylabel("Residuals",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.show()
 
#bar plot of Features and Coefficients
plt.figure(figsize=(8,5))
sns.barplot(data=coefficients,
            x="Feature",
            y="Coefficient",
            palette="viridis",
            )
plt.title("bar plot of Features and Coefficients",fontsize=16,fontweight="bold")
plt.xlabel("Features",fontsize=12,fontweight="bold")
plt.ylabel("Coefficients",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.show() 
 
#Representing Actual sales vs Predicted sales
plt.figure(figsize=(8,5))
plt.scatter(y_test,
            y_pred,
            color = "royalblue",
            edgecolor="black",
            alpha=0.7)
plt.plot(
    [y_test.min(),y_test.max()],    #this draws the ideal prediction line were Actual sales = Predicted sales
    [y_test.min(),y_test.max()],
    linestyle="--",
    linewidth=2,
    color="red"
)
plt.title("Representing Actual sales vs Predicted sales",fontsize=16,fontweight="bold")
plt.xlabel("Actual sales",fontsize=12,fontweight="bold")
plt.ylabel("Predicted sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.3,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.show() 
#testing the new data on our model
new_data = pd.DataFrame({
    "TV" : [230,30,5],
    "Radio" : [30,300,15],
    "Newspaper" : [69,20,55]
})
prediction = model.predict(new_data) #predict the sales of new features entries
new_data["predicted sales"] = prediction  #made new column "predicted sales" for showing sales for each multiple values that we entered
print(new_data)  #print the new data with predicted sales

#saved the trained data
joblib.dump(model,"Sales_prediction_model.pkl")
#load the model 
loaded_model = joblib.load("Sales_prediction_model.pkl")