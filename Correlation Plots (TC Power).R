
library(corrplot)

tc_pwr_day <- read.csv("tc_pwr_day.csv")
tc_pwr_day_synth <- read.csv("tc_pwr_day_synth.csv")

real_cor <- cor(tc_pwr_day[2:9])
colnames(real_cor) <- c("Temp", "Humidity", "Wind Speed", "Gen Diff Flows", "Diff Flows", "Zone 1 Power", "Zone 2 Power", "Zone 3 Power")
rownames(real_cor) <- c("Temp", "Humidity", "Wind Speed", "Gen Diff Flows", "Diff Flows", "Zone 1 Power", "Zone 2 Power", "Zone 3 Power")

corrplot.mixed(real_cor, upper = 'color', lower = 'number',
               title = 'Real Data', mar = c(0, 0, 2, 0),
               lower.col = 'black', number.cex = .9, 
               tl.pos = 'lt', tl.cex = .8, tl.col = 'black')


synth_cor <- cor(tc_pwr_day_synth[2:9])
colnames(synth_cor) <- c("Temp", "Humidity", "Wind Speed", "Gen Diff Flows", "Diff Flows", "Zone 1 Power", "Zone 2 Power", "Zone 3 Power")
rownames(synth_cor) <- c("Temp", "Humidity", "Wind Speed", "Gen Diff Flows", "Diff Flows", "Zone 1 Power", "Zone 2 Power", "Zone 3 Power")

corrplot.mixed(synth_cor, upper = 'color', lower = 'number',
               title = 'Synthetic Data', mar = c(0, 0, 2, 0),
               lower.col = 'black', number.cex = .9, 
               tl.pos = 'lt', tl.cex = .8, tl.col = 'black')
