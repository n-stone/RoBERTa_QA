ROBERTA_PATH = "klue/roberta-base"
MAX_LEN = 40
PADDING = "max_length"
TRUNCATION = True
TRAIN_DESCRIPTION = "Conversation chatbot training by roberta"
TEST_DESCRIPTION = "Consulation chatbot based on Roberta"
CHAT_HELP = "response generation on given user input"
TEST_HELP = "for test"
MODEL_SAVE_PATH = "./model/roberta2roberta.pt"
TRAIN_DATA = "./data/Training.xlsx"
TEST_DATA = "./data/Validation.xlsx"
TEST_RESULT_CSV = "./result/chat_result.csv"
TOP_P = 0.95
TOP_K = 80
TEMPERATURE = 0.6
NO_REPEAT_NGRAM_SIZE = 2
NUM_RETURN_SEQUENCE = 3
DO_SAMPLE = True
MAX_LENGTH = 50
EARLY_STOPPING = False
TRAIN_BATCH_SIZE = 32
TRAIN_BATCH_HELP = "batch size for training (default: 32)"
TRAIN_EPOCH = 1
TRAIN_EPOCH_HELP = "epoch for training (default: 20)"
TRAIN_LR = 5e-5
TRAIN_LR_HELP = "The initial learning rate"