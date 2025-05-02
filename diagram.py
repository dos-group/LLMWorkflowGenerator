import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data1 = {
    "falcon-3-10b-instruct": [6.113213594, 4.159478073, 2.236555677, 8.907328229, 1.226320677, 12.02897526, 12.228157083, 5.524849375, 5.084022552],
    "phi-4": [3.055670886, 11.76704974, 8.704876822, 7.523691302, 5.271546823, 5.692187708, 13.44227125, 2.201008177, 6.775233437],
    "qwen-2dot5-14b-instruct": [1.545090729, 2.366231302, 3.293810678, 2.627149375, 1.971901562, 3.849307083, 4.096569844, 1.956806927, 9.058111927],
    "gpt-4o": [1.889654948, 2.226543282, 1.29390349, 1.175422187, 0.855597917, 3.010535833, 1.452993073, 1.914872969, 1.901530729],
    "gpt-4o-mini": [7.368344375, 4.050426198, 2.499460834, 6.209175989, 1.540320885, 3.484008386, 4.98890474, 2.421248698, 3.325916927],
    "gpt-4-turbo": [7.353877813, 4.078254583, 4.529464583, 2.077671615, 8.161520312, 8.690924739, 4.060953386, 13.700647136, 6.080700208],
    "gpt-4.5-preview-2025-02-27": [3.03546677, 5.890060365, 5.084214011, 6.264463802, 5.495807656, 8.457108645, 8.025357188, 4.149997812, 18.758590104]
}

data2 = {
    "falcon-3-10b-instruct": [339.572188, 346.614114, 359.732292, 360.038125, 359.977604, 368.306823, 353.909479, 347.567604, 344.630572],
    "phi-4": [379.23349, 387.532344, 414.411354, 395.552344, 384.411615, 378.985729, 407.436198, 440.584062, 397.849844],
    "qwen-2dot5-14b-instruct": [429.478073, 385.947188, 386.991771, 402.147084, 382.678854, 373.450625, 405.784271, 379.904687, 369.024219],
    "gpt-4o": [619.529896, 570.449323, 540.422448, 451.980573, 609.636302, 641.714322, 444.470104, 504.396771, 476.554844],
    "gpt-4o-mini": [565.931771, 425.735313, 540.865365, 476.434948, 583.036927, 461.581146, 523.948802, 468.587812, 438.512083],
    "gpt-4-turbo": [678.424167, 1097.061615, 806.986198, 619.234896, 1758.288802, 736.542135, 713.5675, 966.869063, 571.358281],
    "gpt-4.5-preview-2025-02-27": [1077.005885, 884.490469, 726.329584, 783.776927, 859.48901, 858.798333, 815.109844, 1021.890104, 1074.428125]
}

df1 = pd.DataFrame(data1)
df1['Point'] = range(1, len(df1) + 1)
df1_long = df1.melt(id_vars='Point', var_name='Model', value_name='Response Time (s)')

df2 = pd.DataFrame(data2)
df2['Point'] = range(1, len(df2) + 1)
df2_long = df2.melt(id_vars='Point', var_name='Model', value_name='Time to First Token (ms)')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

sns.swarmplot(
    data=df1_long,
    x='Model',
    y='Response Time (s)',
    hue='Point',
    palette="tab10",
    dodge=False,
    size=7,
    ax=ax1
)

ax1.set_title("")
ax1.set_xlabel("")
ax1.set_ylabel("Response Time (s)")
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

sns.swarmplot(
    data=df2_long,
    x='Model',
    y='Time to First Token (ms)',
    hue='Point',
    palette="tab10",
    dodge=False,
    size=7,
    ax=ax2
)

ax2.set_title("")
ax2.set_xlabel("")
ax2.set_ylabel("Time to First Token (ms)")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

handles, labels = ax1.get_legend_handles_labels()

ax1.get_legend().remove()
ax2.get_legend().remove()

for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

fig.legend(handles, labels, title="Intention", bbox_to_anchor=(0.5, 0.95), loc='center', ncol=9)

plt.tight_layout(pad=0, rect=(0, 0, 0, 0.875))

plt.savefig("diagram0.pdf")
