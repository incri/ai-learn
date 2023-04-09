# helper functions


from sklearn import decomposition
from sklearn.model_selection import train_test_split

def split_and_pca(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.33, 
                                                        random_state=42)    

    pca = decomposition.PCA(n_components=nof_prin_components, whiten=True).fit(X)
    
    X_pca = pca.transform(X)
    X_train_pca = pca.transform(X_train) 
    X_test_pca = pca.transform(X_test)
    
    return X_pca, X_train_pca, y_train, X_test_pca, y_test
    

def get_min_max(data_2d):
    x_min, x_max = data_2d[:, 0].min() - 0.5, data_2d[:, 0].max() + 0.5
    y_min, y_max = data_2d[:, 1].min() - 0.5, data_2d[:, 1].max() + 0.5
    return x_min, x_max, y_min, y_max  



# plot data and classifier decision-boundaries

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.inspection import DecisionBoundaryDisplay

figure = plt.figure(figsize=(18, 6))

i = 1

# iterate over datasets
for ds_cnt, ds in enumerate(datasets):
    print('Current dataset:', dataset_names[ds_cnt])
    # preprocess dataset, split into training and test part
    X, y = ds
   
    X_pca, X_train_pca, y_train, X_test_pca, y_test = split_and_pca(X, y)
    
    # get min, max values for plot axis    
    x_min, x_max, y_min, y_max = get_min_max(X_pca)
    '''
    print("x_min", x_min, 
          "x_max", x_max, 
          "y_min", y_min, 
          "y_max", y_max)
    '''

    # ploting the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(["#FF0000", "#0000FF"])
    
    # setting no. of rows and column for the plot
    ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
    
    # label for first column
    if ds_cnt == 0:
        ax.set_title("Input data")
        
    # plot the training points
    ax.scatter(X_train_pca[:, 0], 
               X_train_pca[:, 1], 
               c=y_train, 
               cmap=cm_bright, 
               edgecolors="k")
    
    # plot the testing points with alpha value (the data points will become lighter)
    ax.scatter(
        X_test_pca[:, 0], 
        X_test_pca[:, 1], 
        c=y_test, 
        cmap=cm_bright, 
        alpha=0.6, 
        edgecolors="k"
    )
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1
    
    
    # plot sub-plots with train-test points and classifier outputs
    
    # iterate over classifiers
    for name, clf in zip(names, classifiers):
        print('    Current classifier:', name, end = ' ')
        
        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)

        clf = make_pipeline(StandardScaler(), clf)
        
        clf.fit(X_train_pca, y_train)
        
        score = clf.score(X_test_pca, y_test)
        print('score', f'{score:.2f}')
        
        # draw decision boundary
        DecisionBoundaryDisplay.from_estimator(clf, 
                                               X_pca, 
                                               cmap=cm, 
                                               alpha=0.8, 
                                               ax=ax, 
                                               eps=0.5)

        # plot the training points
        
        ax.scatter(X_train_pca[:, 0], 
                   X_train_pca[:, 1], 
                   c=y_train, 
                   cmap=cm_bright, 
                   edgecolors="k")
        
        
        # plot the testing points
        ax.scatter(X_test_pca[:, 0],
                   X_test_pca[:, 1],
                   c=y_test,
                   cmap=cm_bright,
                   edgecolors="k",
                   alpha=0.6)

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_xticks(())
        ax.set_yticks(())
        if ds_cnt == 0:
            ax.set_title(name)
            
        ax.text(x_max - 0.3,
                y_min + 0.3,
                ("%.2f" % score).lstrip("0"),
                size=15,
                horizontalalignment="right")
        i += 1

plt.tight_layout()
plt.show()