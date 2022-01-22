import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# DATA SOURCE: https://ourworldindata.org/covid-cases
df = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])
saudi_df = df[(df['location'] == 'Saudi Arabia')]

#############################################################################################
# Covid-19 cases are rising because there are more people getting tested!?

# FIRST LETS  FIND IF THE NUMBER OF PCR TESTS IS ACTUALY HIGHER THAN BEFORE
temp = saudi_df.melt(id_vars='date', value_vars = ['new_cases','new_tests' ], var_name='PCR TESTS', value_name='Count')

fig = px.area(temp, x = 'date', y = 'Count', color='PCR TESTS', height=600, title='NUMBER OF PCR TEST IN SAUDI ARABIA')
fig.update_layout(xaxis_rangeslider_visible=True, title_x=0.5)
# fig.show(renderer='browser')
fig.write_image("images/NUMBER_OF_PCR_TEST_IN_SAUDI_ARABIA.png")
fig.write_html("html/NUMBER_OF_PCR_TEST_IN_SAUDI_ARABIA.html")

# NOW LET FIND IF THE % OF POSITIVE TEST IS CHAGES OVER TIME
saudi_df['case_test_ratio'] = 100 * saudi_df['new_cases'] / saudi_df['new_tests']
temp = saudi_df.melt(id_vars='date', value_vars = ['case_test_ratio' ], var_name='Positive PCR Tests', value_name='% positive PCR Tests')

fig = px.area(temp, x = 'date', y = '% positive PCR Tests', color='Positive PCR Tests', height=600, title='% OF POSITIVE TEST IS CHAGES OVER TIME IS SAUDI ARABIA')
fig.update_layout(xaxis_rangeslider_visible=True, title_x=0.5)
# fig.show(renderer='browser')
fig.write_image("images/Positive_PCR_Tests.png")
fig.write_html("html/Positive_PCR_Tests.html")