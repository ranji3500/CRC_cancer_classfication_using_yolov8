from ultralytics import YOLO


model = YOLO(r'crc_weight.pt')

model(r"F:\My_learning\computer_vision\CRC_cancer_prediction\test\01_TUMOR\1DAD_CRC-Prim-HE-07_022.tif_Row_1_Col_1.tif")