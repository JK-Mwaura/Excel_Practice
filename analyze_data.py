
import pandas as pd
from scipy.stats import mode

def analyze_excel_data(file_path):
    """
    Reads an Excel file, calculates mean, median, mode, and standard deviation
    for numerical columns, and prints the results.
    """
    try:
        # Specify header=1 to use the second row as the header (0-indexed)
        df = pd.read_excel(file_path, header=1)
    except FileNotFoundError:
        print(f"Error: The file \'{file_path}\' was not found.")
        return
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    print(f"\n--- Analysis for {file_path} ---")

    numerical_cols = df.select_dtypes(include=['number']).columns

    if numerical_cols.empty:
        print("No numerical columns found for analysis.")
        return

    for col in numerical_cols:
        print(f"\nColumn: {col}")
        # Drop NaN values for accurate calculations
        series = df[col].dropna()

        if series.empty:
            print("  No data to analyze in this column.")
            continue

        mean_val = series.mean()
        median_val = series.median()
        
        # Handle mode calculation: mode() returns a ModeResult object
        # .mode attribute is an array of modes, even if there's only one
        mode_result = mode(series, keepdims=True)
        mode_val = mode_result.mode[0] if len(mode_result.mode) > 0 else 'N/A'
        
        std_dev_val = series.std()

        print(f"  Mean: {mean_val:.2f}")
        print(f"  Median: {median_val:.2f}")
        print(f"  Mode: {mode_val}")
        print(f"  Standard Deviation: {std_dev_val:.2f}")

if __name__ == "__main__":
    excel_file = "/home/ubuntu/upload/mouth_swab_Clean_Data.xlsx"
    analyze_excel_data(excel_file)
