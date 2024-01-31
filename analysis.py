import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency,mode, skew, kurtosis,norm, expon, uniform, binom, poisson
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import pandas as pd
# Function to read CSV file
def read_csv():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a CSV file
    csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])

    # Check if a file was selected
    if csv_file_path:
        # Read the CSV file and create a DataFrame
        df = pd.read_csv(csv_file_path)
        return df
    else:
        print("No file selected.")
        return None

def get_save_location():
    root = tk.Tk()
    root.withdraw()
    save_location = filedialog.askdirectory(title="Select Save Location for graphs")
    root.destroy()
    return save_location

# Function to calculate mean
def calculate_mean(data, column_name):
    mean_value = data.mean()
    print(f"Mean for '{column_name}': {mean_value}")
    return mean_value

# Function to calculate mode
def calculate_mode(data, column_name):
    mode_value = data.mode().iloc[0]
    print(f"Mode for '{column_name}': {mode_value}")
    return mode_value

# Function to calculate median
def calculate_median(data, column_name):
    median_value = data.median()
    print(f"Median for '{column_name}': {median_value}")
    return median_value

# Function to calculate minimum
def calculate_minimum(data, column_name):
    min_value = data.min()
    print(f"Minimum for '{column_name}': {min_value}")
    return min_value

# Function to calculate maximum
def calculate_maximum(data, column_name):
    max_value = data.max()
    print(f"Maximum for '{column_name}': {max_value}")
    return max_value

# Function to calculate quartiles
def calculate_quartiles(data, column_name):
    q1 = np.percentile(data, 25, interpolation='midpoint')
    q3 = np.percentile(data, 75, interpolation='midpoint')
    print(f"Q1 for '{column_name}': {q1}")
    print(f"Q3 for '{column_name}': {q3}")
    return q1, q3

# Function to calculate sum of squared errors
def calculate_sse(data, column_name):
    mean_value = calculate_mean(data, column_name)
    sse_value = np.sum((data - mean_value) ** 2)
    print(f"Sum of Squared Errors for '{column_name}': {sse_value}")
    return sse_value

# Function to calculate skewness
def calculate_skewness(data, column_name):
    skewness_value = data.skew()
    print(f"Skewness for '{column_name}': {skewness_value}")
    return skewness_value

# Function to calculate kurtosis
def calculate_kurtosis(data, column_name):
    kurtosis_value = data.kurtosis()
    print(f"Kurtosis for '{column_name}': {kurtosis_value}")
    return kurtosis_value

# Function to calculate sample standard deviation
def calculate_sample_std_dev(data, column_name):
    std_dev_value = data.std(ddof=1)
    print(f"Sample Standard Deviation for '{column_name}': {std_dev_value}")
    return std_dev_value

# Function to calculate population standard deviation
def calculate_population_std_dev(data, column_name):
    std_dev_value = data.std()
    print(f"Population Standard Deviation for '{column_name}': {std_dev_value}")
    return std_dev_value

# Function to calculate sample variance
def calculate_sample_variance(data, column_name):
    variance_value = data.var(ddof=1)
    print(f"Sample Variance for '{column_name}': {variance_value}")
    return variance_value

# Function to calculate population variance
def calculate_population_variance(data, column_name):
    variance_value = data.var()
    print(f"Population Variance for '{column_name}': {variance_value}")
    return variance_value



# Function to get user input for plot generation
def get_plot_choice(plot_type):
    user_input = input(f"Do you want to generate {plot_type} plot? (yes/no): ").lower()
    return user_input == 'yes'

def get_x_y_values():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter the x and y column names
    x_column = input("Enter the x column name: ")
    y_column = input("Enter the y column name: ")
    
      # Explicitly destroy the Tkinter window
    root.destroy()
    
    return x_column, y_column

def get_save_location():
    root = tk.Tk()
    root.withdraw()
    save_location = filedialog.askdirectory(title="Select Save Location")
    root.destroy()
    return save_location

# Function to generate scatter plot and save as PNG
def generate_scatter_plot(data, column_x, column_y, save_location):
    plt.scatter(data[column_x], data[column_y])
    plt.title(f"Scatter Plot for '{column_x}' vs '{column_y}'")
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.savefig(f"{save_location}/scatter_plot.png")
    plt.show()

# Function to generate line plot and save as PNG
def generate_line_plot(data, column_x, column_y, save_location):
    plt.plot(data[column_x], data[column_y])
    plt.title(f"Line Plot for '{column_x}' vs '{column_y}'")
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.savefig(f"{save_location}/line_plot.png")
    plt.show()

# Function to generate bar plot and save as PNG
def generate_bar_plot(data, column_x, column_y, save_location):
    plt.bar(data[column_x], data[column_y])
    plt.title(f"Bar Plot for '{column_x}' vs '{column_y}'")
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.savefig(f"{save_location}/bar_plot.png")
    plt.show()

# Function to generate box plot and save as PNG
def generate_box_plot(data, column_x, column_y, save_location):
    plt.boxplot([data[data[column_x] == category][column_y] for category in data[column_x]], vert=False)
    plt.title(f"Box Plot for '{column_y}' grouped by '{column_x}'")
    plt.xlabel(column_y)
    plt.savefig(f"{save_location}/box_plot.png")
    plt.show()


# Function to generate histogram and save as PNG
def generate_histogram(data, column_name, save_location):
    plt.hist(data, bins=20, edgecolor='black')
    plt.title(f"Histogram for '{column_name}'")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(f"{save_location}/{column_name}_histogram.png")
    plt.show()
    plt.close()


# Function to print statistics for a column
def print_column_statistics(data, column_name):
    try:
        column_data = data[column_name].astype(float)
        calculate_mean(column_data, column_name)
        calculate_mode(column_data, column_name)
        calculate_median(column_data, column_name)
        calculate_minimum(column_data, column_name)
        calculate_maximum(column_data, column_name)
        calculate_quartiles(column_data, column_name)
        calculate_sse(column_data, column_name)
        calculate_skewness(column_data, column_name)
        calculate_kurtosis(column_data, column_name)
        calculate_sample_std_dev(column_data, column_name)
        calculate_population_std_dev(column_data, column_name)
        calculate_sample_variance(column_data, column_name)
        calculate_population_variance(column_data, column_name)
        
        print("\n" + "=" * 40 + "\n")
        
      
         
    except Exception as e:
        print(f"\nUnable to process '{column_name}': {str(e)}")
        
# Main function
# Main function
def main():
    # Read CSV file
    df = read_csv()

    if df is not None:
        # Iterate over each column and print statistics
        for column_name in df.columns:
            print_column_statistics(df, column_name)

        # Ask for x and y columns after all computations
        x_column, y_column = get_x_y_values()

        # Ask for the save location
        save_location = get_save_location()

        if get_plot_choice("scatter"):
            generate_scatter_plot(df, x_column, y_column, save_location)

        if get_plot_choice("line"):
            generate_line_plot(df, x_column, y_column, save_location)

        if get_plot_choice("bar"):
            generate_bar_plot(df, x_column, y_column, save_location)

        if get_plot_choice("box"):
            generate_box_plot(df, x_column, y_column, save_location)

        if get_plot_choice("histogram"):
            generate_histogram(df[y_column], y_column, save_location)

# Run the main function
if __name__ == "__main__":
    main()
