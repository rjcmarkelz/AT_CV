library(ggplot2)
setwd("~/git.repos/arabidopsis_cv/data")

size <- read.csv("plant-growth.csv", header = FALSE)
names(size) <- paste(c("group","image","PixelArea"))
head(size)
size$treatment <- sub("(\\w+)(Group)(\\d)(\\w+)", "\\4", size$group)
size$hour <- sub("(\\w+)(Group)(\\d)(\\w+)", "\\1", size$group)
size$date <- as.Date(sub("(\\w+)(_)(\\w+)(.jpg)", "\\1", size$image))
str(size)
size$PixelArea <- size$PixelArea/1000

qplot(data = size, y = PixelArea, x = date, color = trt)

out <- ggplot(size, aes(x = date, y = PixelArea, color = treatment))
out <- out + geom_point() + geom_smooth()
out
?ggsave
ggsave("Rossette-Growth.pdf")