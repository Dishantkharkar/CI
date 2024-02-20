import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'pineapple']
counts = [155, 433, 30]
bar_labels = ['red', 'orange', 'green']
bar_colors = ['tab:red', 'tab:blue', 'tab:green']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.savefig('bars.png', bbox_inches='tight')

cat = ["bored", "happy", "happy", "happy", "happy", "bored"]
dog = ["bored", "bored", "bored", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')