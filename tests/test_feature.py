import pytest
import project1_phase2
from project1_phase2 import unredactor

def tests_cleaningData():
    
    filepath = '/project/cs5293sp19-project1-phase2/aclImdb/train/pos'
    
    count_of_files_to_extract=10

    filenames,entities,files = unredactor.read_textfiles_from_directory(filepath, '.txt',count_of_files_to_extract)
    
    train , test = unredactor.Train_and_test_cases(filenames,entities,files,0.6,count_of_files_to_extract)
    
    train_filename = train[0][:]
    train_entity = train[1][:]
    train_files = train[2][:]

    test_filename = test[0][:]
    test_entity = test[1][:]
    test_files = test[2][:]

    # Removing <BR> and some few unneccesary things by cleaning
    train_files = unredactor.Removing_uneccesary(train_files)
    test_files = unredactor.Removing_uneccesary(test_files)
    
    train_filename,train_entity,train_files,train_labels = unredactor.cleaning_TrainingSet(train_filename,train_entity,train_files)
    redacted_file_test,test_labels = unredactor.redacted_of_files(test_files,train_labels)
    redacted_file_train,train_labels = unredactor.redacted_of_files(train_files,train_labels)


    freqnt_words = unredactor.Frequent_words(redacted_file_train)
    freqnt_words = unredactor.Removing_uneccesary_braces(freqnt_words)
    X_train = unredactor.Feature_selection(redacted_file_train,freqnt_words)
    
        
    assert len(X_train[0]) == 8 #8 features 
