import ProcessData
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(np.array(all_tracks_scaled),
                                                    np.array(genre),
                                                    test_size=0.33,
                                                    random_state=42)


