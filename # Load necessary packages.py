# Load necessary packages
library(dplyr)

# Step 1: Load the data
features <- read.table("UCI HAR Dataset/features.txt")
activity_labels <- read.table("UCI HAR Dataset/activity_labels.txt", col.names = c("id", "activity"))

# Load training data
subject_train <- read.table("UCI HAR Dataset/train/subject_train.txt", col.names = "subject")
x_train <- read.table("UCI HAR Dataset/train/X_train.txt")
y_train <- read.table("UCI HAR Dataset/train/y_train.txt", col.names = "activity_id")

# Load test data
subject_test <- read.table("UCI HAR Dataset/test/subject_test.txt", col.names = "subject")
x_test <- read.table("UCI HAR Dataset/test/X_test.txt")
y_test <- read.table("UCI HAR Dataset/test/y_test.txt", col.names = "activity_id")

# Step 2: Merge the training and test datasets
subjects <- rbind(subject_train, subject_test)
activities <- rbind(y_train, y_test)
data <- rbind(x_train, x_test)

# Apply feature names
colnames(data) <- features$V2

# Combine all data
merged_data <- cbind(subjects, activities, data)

# Step 3: Extract measurements on the mean and standard deviation
selected_features <- grep("mean\\(\\)|std\\(\\)", features$V2)
selected_data <- merged_data[, c(1, 2, selected_features + 2)]

# Step 4: Use descriptive activity names
selected_data <- merge(selected_data, activity_labels, by.x = "activity_id", by.y = "id")
selected_data <- selected_data[, -1]

# Step 5: Label the dataset with descriptive variable names
names(selected_data) <- gsub("^t", "Time", names(selected_data))
names(selected_data) <- gsub("^f", "Frequency", names(selected_data))
names(selected_data) <- gsub("Acc", "Accelerometer", names(selected_data))
names(selected_data) <- gsub("Gyro", "Gyroscope", names(selected_data))
names(selected_data) <- gsub("Mag", "Magnitude", names(selected_data))
names(selected_data) <- gsub("BodyBody", "Body", names(selected_data))

# Step 6: Create a tidy dataset with the average of each variable for each activity and each subject
tidy_data <- selected_data %>%
  group_by(subject, activity) %>%
  summarise(across(everything(), mean), .groups = "drop")

# Save the tidy dataset
write.table(tidy_data, "tidy_data.txt", row.name = FALSE)
