 # Exploratory Data Analysis

## Distribution of TV Advertising

![Distribution of TV Advertising](output\graphs\01_histogram_tv_advertising.png)

### Insights
* Most records are concentrated between **200 and 221**, making it the most common TV advertising budget range in the dataset.
* TV advertising budgets between **0 and 123** also appear frequently, showing that many observations have low to moderate TV spending.
* The **173 to 246** range contains a good number of records, indicating that higher TV advertising budgets are also well represented.
* Very high TV advertising budgets between **246 and 270** have the fewest records, making them the least common in the dataset.
* Overall, the data is spread across almost the entire TV advertising range, with more records concentrated in the middle and fewer at the highest values.

## Distribution of Radio Advertising

![Distribution of Radio Advertising](output\graphs\02_histogram_radio_advertising.png)

### Insights

* Most records are concentrated between **0 and 4**, making it the most common radio advertising budget range in the dataset.
* Radio advertising budgets between **4 and 14** also have many records, showing that lower advertising budgets are quite common.
* A good number of records fall between **20 and 29**, indicating moderate radio advertising budgets are also well represented.
* The **29 to 34** range has the fewest records, making it the least common advertising budget range.
* Overall, the records are spread across different radio advertising budget ranges, with more observations at lower budgets and fewer at the higher end.

## Distribution of Newspaper Advertising

![Distribution of Newspaper Advertising](output\graphs\03_histogram_newspaper_advertising.png)

### Insights

* Most records are concentrated between **0 and 11**, making it the most common newspaper advertising budget range in the dataset.
* Newspaper advertising budgets between **11 and 34** also have many records, showing that low to moderate spending is quite common.
* The number of records gradually decreases as the newspaper advertising budget increases.
* Very high newspaper advertising budgets above **79** have only a few records, making them the least common in the dataset.
* Overall, the records are mostly concentrated at lower newspaper advertising budgets, while higher spending values appear much less frequently.

## Relation between sales and TV advertisement

![Relation between sales and TV advertisement](output\graphs\04_scatterplot_tv&sales.png)

### Insight

* Sales show a **moderately positive** relationship with TV advertising.
* As TV advertising increases, sales generally increase.
* Most records are concentrated in the **0–100** TV advertising range.
* Beyond **100**, the number of records decreases, but the positive trend continues.
* Overall, higher TV advertising is associated with higher sales.


## Relation between sales and Radio advertisement

![Relation between sales and Radio advertisement](output\graphs\05_scatterplot_radio&sales.png)

### Insight

* Sales have a **positive but below-moderate** relationship with radio advertising.
* As radio advertising increases, sales generally increase.
* Most records are concentrated at **lower radio advertising budgets** (below 30).
* A few outliers show **high radio advertising spend but relatively low sales**.
* Overall, higher radio advertising is generally associated with higher sales, but the relationship is weaker than TV advertising.


## Relation between sales and Newspaper advertisement

![Relation between sales and Newspaper advertisement](output\graphs\06_scatterplot_newspaper&sales.png)

### Insight

* Sales show a **moderate positive** relationship with newspaper advertising.
* The data points are widely scattered, indicating a weaker relationship than TV advertising.
* Most records have **newspaper advertising below 50** and **sales below 15**.
* A few records achieve **higher sales (above 20)** with newspaper advertising below **50–60**.
* Only a couple of outliers are present at the highest newspaper advertising values.

## Relation between All numerical values by Heatmap

![Relation between All numerical values by heatmap](output\graphs\07_heatmap.png)

### Insight

* TV and Radio have almost no relationship, which means spending more on TV does not mean more spending on Radio.
* TV and Newspaper also have almost no relationship, showing these two advertising channels are mostly independent.
* TV has the strongest positive relationship with Sales (0.78), indicating TV advertising contributes the most to increasing      sale.
* Radio has a moderate positive relationship with Sales (0.58), while Newspaper has only a weak positive relationship (0.23), so Radio affects sales more than Newspaper.
* Overall, TV is the most important advertising channel for sales, followed by Radio, while Newspaper has the least impact on sales.


## Sales distribution of records by Boxplot

![Sales distribution of records by Boxplot](output\graphs\08_boxplot_sales.png)

### Insight

* The median sales value is around 12, which means half of the sales records are below 12 and the other half are above 12.
* Most sales values are between 10 and 16, showing where the majority of the data is concentrated.
* Sales values range from about 1 to 26, indicating that the dataset contains both low and high sales values.
* No outliers are present, which means there are no unusually high or unusually low sales records.
* The sales data shows a moderate spread, meaning sales vary across records but stay within a reasonable range.


## Residualplot predicted sales

![residualplot predicted sales](output\graphs\09_residualplot_predictedsales.png)

### Insight

* The residuals are scattered above and below the zero line, showing that the model does not consistently overpredict or underpredict sales.
* Most residuals are close to zero, which means the model predicts sales accurately for most records.
* A few points are farther from the zero line, indicating larger prediction errors for some observations.
* These larger errors may occur because some factors affecting sales are not included in the dataset.
* Overall, the residual plot shows that the Linear Regression model provides a good fit and predicts sales reasonably well, with some scope for improvement.


## Bar plot of Features and Coefficients

![bar plot of Features and Coefficients](output\graphs\10_barplot_features&coefficients.png)

### Insight

* Radio has the highest positive coefficient, indicating it has the strongest impact on increasing sales.
* TV also has a positive coefficient, meaning higher TV advertising generally leads to higher sales.
* Newspaper has a very small negative coefficient, suggesting it has little or no meaningful effect on sales.
* TV and Radio are the most influential advertising channels in the Linear Regression model.
* Overall, the model indicates that Radio contributes the most to sales, followed by TV, while Newspaper has the least impact.

## Representing Actual sales vs Predicted sales

![Representing Actual sales vs Predicted sales](output\graphs\11_actual_vs_predicted_sales.png)

### Insight

* Most points are close to the ideal line, showing that the model predicts sales accurately for most records.
* Some points overlap, indicating that their actual and predicted sales values are almost the same.
* A few points are farther from the ideal line, showing larger prediction errors for those observations.
* No clear systematic pattern is visible, meaning the model does not consistently overpredict or underpredict sales.
* Overall, the Linear Regression model performs well and provides reliable sales predictions for most records.




# Machine Learning LinearRegression model

## Model Evaluation Metrics

### Insights

* The model achieved an R² score of 0.899, which means it explains about 90% of the variation in sales, indicating a strong model fit.
* The MAE is 1.46, meaning the model's predictions differ from the actual sales by about 1.46 units on average.
* The RMSE is 1.78, showing that the prediction errors are generally small and there are no major errors for most observations.
* The MSE is 3.17, indicating that the overall prediction error is low and the model performs well on the test data.
* Overall, the evaluation metrics show that the Linear Regression model predicts sales accurately and provides reliable results for most observations.

## Model coeffcients

### Insights

* Radio has the highest positive coefficient (0.189), indicating it has the strongest positive impact on sales.
* TV also has a positive coefficient (0.045), meaning increasing TV advertising generally increases sales.
* Newspaper has a very small positive coefficient (0.003), showing it has only a minimal impact on sales.
* All coefficients are positive, meaning increasing advertising spend is associated with an increase in predicted sales.
* Overall, the model suggests that Radio contributes the most to sales, followed by TV, while Newspaper has the least influence.

# Business Insights


* Increase investment in TV and Radio advertising, as these channels have the strongest positive impact on sales.
* Review the Newspaper advertising budget, as it contributes very little to increasing sales compared to TV and Radio.
* Use the trained Linear Regression model to estimate future sales before planning advertising campaigns and budgets.
* Focus marketing budgets on high-performing advertising channels to improve return on investment (ROI).
* Use sales predictions to support business decisions, such as campaign planning, budget allocation, and sales forecasting.

## Project Limitations

This project successfully completed all analyses and modeling tasks that were supported by the provided dataset.
However, a few of the originally expected objectives could not be implemented because the dataset did not contain the required features.

### For example:

* Customer target segmentation requires demographic or customer-related attributes.
* Platform-wise performance analysis requires platform-specific advertising data.
* Customer retention analysis requires historical customer activity data.
* Time-series sales forecasting requires date or timestamp information.

These features were not available in the provided dataset; therefore, the corresponding analyses and models were beyond the scope of this project.