# tidy-data-set-
Getting and Cleaning Data Course Project
# README.md

## Overview
This repository contains the script and associated documentation for processing and tidying the Human Activity Recognition Using Smartphones Dataset. The purpose of this project is to demonstrate the ability to collect, clean, and prepare data for subsequent analysis.

## Contents

1. **run_analysis.R**: An R script that performs the following operations:
   - Merges the training and test datasets to create a single dataset.
   - Extracts only the measurements on the mean and standard deviation for each measurement.
   - Applies descriptive activity names to name the activities in the dataset.
   - Appropriately labels the dataset with descriptive variable names.
   - Creates a second, independent tidy dataset with the average of each variable for each activity and each subject.

2. **tidy_data.txt**: A tidy dataset containing the average of each variable for each activity and subject. This dataset is the output of `run_analysis.R`.

3. **CodeBook.md**: A codebook describing the variables, transformations, and process used to clean and tidy the data.

## Instructions

1. Clone the repository and ensure the Samsung data is in your working directory.
2. Run the `run_analysis.R` script in R.
3. The script will generate `tidy_data.txt` as output.

## Dependencies

The script requires the following R packages:
- `dplyr`

Install them using:
```R
install.packages("dplyr")
```

Ensure the dataset is unzipped and placed in the working directory with the structure:
```
UCI HAR Dataset/
```

# CodeBook.md

## Dataset Description
The dataset represents data collected from the accelerometers of the Samsung Galaxy S smartphone. It contains data on human activities, such as walking, sitting, and standing.

### Variables

1. **subject**: Identifier for the subject performing the activity (range: 1-30).
2. **activity**: Descriptive activity name (e.g., Walking, Sitting).
3. **TimeBodyAccelerometerMeanX**: Mean value of body acceleration along the X-axis (time domain).
4. **TimeBodyAccelerometerMeanY**: Mean value of body acceleration along the Y-axis (time domain).
5. **TimeBodyAccelerometerMeanZ**: Mean value of body acceleration along the Z-axis (time domain).
6. **FrequencyBodyGyroscopeMeanX**: Mean value of body gyroscope data along the X-axis (frequency domain).

*(Additional variables follow the same naming convention, representing measurements of means and standard deviations for accelerometer and gyroscope data in time and frequency domains.)*

### Transformations

1. **Merged Datasets**: Combined training and test datasets using `rbind`.
2. **Extracted Mean/Std Variables**: Filtered columns to include only measurements containing `mean()` or `std()`.
3. **Descriptive Activity Names**: Mapped activity labels to descriptive names using the activity labels file.
4. **Renamed Columns**: Replaced abbreviations (e.g., `t` with `Time`, `Acc` with `Accelerometer`) for clarity.
5. **Created Tidy Dataset**: Averaged each variable for each activity and subject.

## How to Use the Tidy Dataset

- Load the tidy dataset into R using:
```R
data <- read.table("tidy_data.txt", header = TRUE)
```

