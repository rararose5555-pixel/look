library(ggplot2)

data <- read.csv("cars.csv")

p1 <- ggplot(data, aes(x = Weight, y = Mileage)) +
  geom_point(color = "steelblue", size = 3) +
  geom_smooth(method = "lm", color = "red", se = FALSE) +
  labs(title = "Car Weight vs Mileage", x = "Weight (lbs)", y = "Mileage (mpg)")
print(p1)
readline(prompt = "Press Enter for next plot...")

p2 <- ggplot(data, aes(x = factor(Cylinders))) +
  geom_bar(fill = "darkorange") +
  labs(title = "Number of Cars by Cylinders", x = "Cylinders", y = "Count")
print(p2)
readline(prompt = "Press Enter for next plot...")

p3 <- ggplot(data, aes(x = Mileage)) +
  geom_histogram(bins = 6, fill = "steelblue", color = "white") +
  labs(title = "Distribution of Mileage", x = "Mileage (mpg)", y = "Frequency")
print(p3)