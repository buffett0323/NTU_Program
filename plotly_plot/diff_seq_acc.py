import plotly.graph_objects as go
import plotly.io as pio

# Data from the user
sequences = ['3', '4', '5', '6', '7', '8']

# Accuracies list
hybrid_gru_accuracies = [87.68, 84.2, 85.99, 82.67, 86.14, 81.81]
hybrid_gru_adj_accuracies = [96.04, 94.82, 96.01, 94.95, 96.65, 95.33]
basic_accuracies = [84.28, 81.52, 82.96, 79.21, 82.41, 79.73]

# Creating the bar chart for both sets of accuracies
fig = go.Figure()

# Adding Hybrid GRU model accuracies
fig.add_trace(go.Bar(
    x=sequences, 
    y=hybrid_gru_accuracies, 
    name='Hybrid GRU',
    text=hybrid_gru_accuracies, 
    textposition='auto', 
    marker_color='lightblue'
))

# Adding basic model accuracies
fig.add_trace(go.Bar(
    x=sequences, 
    y=basic_accuracies, 
    name='Basic LSTM',
    text=basic_accuracies, 
    textposition='auto', 
    marker_color='lightgreen'
))

# Customizing the layout with a lighter theme
fig.update_layout(
    title='Accuracy Comparison of Hybrid GRU and Basic LSTM Models',
    xaxis_title='Sequence Length',
    yaxis_title='Accuracy (%)',
    yaxis=dict(range=[0, 100]),
    template='plotly_white',
    barmode='group'
)

# Show the plot
fig.show()

# Save the figure to a file
file_path = '../plotly_result/hybrid_vs_basic_accuracy_chart.png'
pio.write_image(fig, file_path)
