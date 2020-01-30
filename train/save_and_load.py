import pandas as pd
import torch
from definition import logger

def save_epoch_result(train_result, valid_result):
    train_dict, train_loss, train_cer = train_result
    valid_dict, valid_loss, valid_cer = valid_result
    train_dict["loss"].append(train_loss)
    train_dict["cer"].append(train_cer)
    valid_dict["loss"].append(valid_loss)
    valid_dict["cer"].append(valid_cer)

    train_df = pd.DataFrame(train_dict)
    valid_df = pd.DataFrame(valid_dict)
    train_df.to_csv("../csv/train_result.csv", encoding='cp949', index=False)
    valid_df.to_csv("../csv/eval_result.csv", encoding='cp949', index=False)

    del train_df, valid_df  # memory deallocation

def save_step_result(train_step_result, loss, cer):
    train_step_result["loss"].append(loss)
    train_step_result["cer"].append(cer)
    train_step_df = pd.DataFrame(train_step_result)
    train_step_df.to_csv("./csv/train_step_result.csv", encoding='cp949', index=False)

    del train_step_df


def load_model(filepath):
    logger.info("Load model..")
    model = torch.load(filepath)
    model.eval()
    logger.info("Load model Succesfuuly completely !!")
    return model