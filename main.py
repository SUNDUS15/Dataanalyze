from data import create_data
data_analyze = create_data()
print("Antal värden:", len(data_analyze))
print("De första tio värdena i data:", data_analyze[:10])

from data import create_data
from diagram import show_histogram
analyze_data = create_data()
print("Antal värden:", len(analyze_data))
print("Första tio värdena:", analyze_data[:10])
show_histogram(analyze_data)
