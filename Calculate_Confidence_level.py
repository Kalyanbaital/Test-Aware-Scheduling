# Calculation of Confidence Level. With 95% certainty our results produce that between 85% and 95% of the cores are tested. 

import numpy as np
from scipy import stats

experiment_count = 10
core_count = 10
task_count = 100  # not used
alpha = 0.05

crit_value = stats.t(df=experiment_count-1).ppf(1.0 - alpha / 2)  # used distribution for sample size < 30

# Result data between 80% and 100% tested cores
cores_tested = [9,9,9,8,9,10,10,8,9,9]
print(f'{cores_tested}')

cores_tested_normalized = cores_tested / core_count 
print(f'{cores_tested_normalized}')

sample_mean = cores_tested_normalized.mean()
print(f'{sample_mean}')

sample_variance = ( (cores_tested_normalized - sample_mean)**2 ).mean()
# aka: mean squared error (MSE)
print(f'{sample_variance}')

standard_deviation = np.sqrt(sample_variance)
print(f'{standard_deviation}')

confidence_plus_minus = crit_value * ( standard_deviation / np.sqrt(experiment_count) )
print(f'Experiment Result: {sample_mean*100:.0f} ±{confidence_plus_minus*100:.1f} % with confidence level of{(1-alpha)*100:.0f} %')
