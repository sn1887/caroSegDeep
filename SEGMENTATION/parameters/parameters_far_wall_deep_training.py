class Parameters:

  def __init__(
          self,
          NB_EPOCH,
          NBPATIENCE_EPOCHS,
          BATCH_SIZE,
          DATA_AUGMENTATION,
          MODEL_SELECTION,
          LEARNING_RATE,
          LOSS,
          PATH_TO_SAVE_PREDICTION_DURING_TRAINING,
          PATCH_HEIGHT,
          PATCH_WIDTH,
          PATH_TO_SAVE_TENSORBOARD,
          PATH_TO_SAVE_RESULTS_PDF_METRICS_WEIGHTS,
          NAME_OF_THE_EXPERIMENT,
          PATH_TO_DATASET
  ):
    self.NB_EPOCH=NB_EPOCH
    self.NBPATIENCE_EPOCHS=NBPATIENCE_EPOCHS
    self.BATCH_SIZE=BATCH_SIZE
    self.DATA_AUGMENTATION=DATA_AUGMENTATION
    self.MODEL_SELECTION=MODEL_SELECTION
    self.LEARNING_RATE=LEARNING_RATE
    self.LOSS=LOSS
    self.PATH_TO_SAVE_PREDICTION_DURING_TRAINING=PATH_TO_SAVE_PREDICTION_DURING_TRAINING
    self.PATCH_HEIGHT=PATCH_HEIGHT
    self.PATCH_WIDTH=PATCH_WIDTH
    self.PATH_TO_SAVE_TENSORBOARD=PATH_TO_SAVE_TENSORBOARD
    self.PATH_TO_SAVE_RESULTS_PDF_METRICS_WEIGHTS=PATH_TO_SAVE_RESULTS_PDF_METRICS_WEIGHTS
    self. NAME_OF_THE_EXPERIMENT=NAME_OF_THE_EXPERIMENT
    self.PATH_TO_DATASET=PATH_TO_DATASET