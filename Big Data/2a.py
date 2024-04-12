    import numpy as np
    import dask.dataframe as dd

    def clean_data(df):
        """
        Clean the dataset by filling missing values with zeros.
        
        Args:
        df (dask.dataframe.DataFrame): Input dataframe.
        
        Returns:
        dask.dataframe.DataFrame: Cleaned dataframe.
        """
        df["Population Staying at Home"] = df["Population Staying at Home"].fillna(0)
        return df

    def explore_data(df):
        """
        Explore the dataset by printing types of columns, count of non-null values,
        and descriptive statistics.
        
        Args:
        df (dask.dataframe.DataFrame): Input dataframe.
        """
        try:
            # Show types of columns
            print("Types of Columns:")
            print(df.dtypes)

            # Count non-null values
            print("\nCount of Non-Null Values:")
            print(df.notnull().sum().compute())

            # Compute descriptive statistics for the whole dataframe
            print("\nDescriptive Statistics for the Whole Dataframe:")
            print(df.describe().compute())

            # Alternatively, compute descriptive statistics for just one column
            print("\nDescriptive Statistics for 'Population Staying at Home':")
            print(df['Population Staying at Home'].describe().compute())

        except Exception as e:
            print("An error occurred during data exploration:", e)

    if __name__ == "__main__":
        # Read data
        df_full = dd.read_csv("Trips_Full Data.csv")
        df = dd.read_csv("Trips_By_Distance.csv")

        # Clean data
        df = clean_data(df)

        # Explore data
        explore_data(df)
