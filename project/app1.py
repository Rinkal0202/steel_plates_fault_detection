import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

# Define features used for prediction
feature_names = [
    'Length', 'Width', 'Area', 'Perimeter', 'Roughness',
    'TextureVariance', 'Compactness', 'Symmetry', 'Curvature',
    'Elongation', 'SurfaceDefectDensity', 'EdgeSharpness'
]

# Clipping ranges based on training data min/max
feature_ranges = {
    'Length': (-6.5, 6.0),
    'Width': (-5.0, 6.2),
    'Area': (-6.1, 6.2),
    'Perimeter': (-5.9, 7.0),
    'Roughness': (-6.2, 6.3),
    'TextureVariance': (-4.9, 5.8),
    'Compactness': (-3.2, 3.2),
    'Symmetry': (-6.2, 5.9),
    'Curvature': (-6.4, 4.5),
    'Elongation': (-2.9, 3.2),
    'SurfaceDefectDensity': (-6.5, 6.5),
    'EdgeSharpness': (-12.5, 12.5)
}

# UI Title
st.title("🛠️ Steel Fault Detector")

# Manual input using sliders or number inputs
values = []
for col in feature_names:
    min_val, max_val = feature_ranges[col]
    val = st.number_input(f"{col}", value=0.0, min_value=min_val, max_value=max_val)
    values.append(val)

# Predict button
if st.button("Predict"):
    # Create input DataFrame
    input_df = pd.DataFrame([values], columns=feature_names)

    # Extra safeguard: clip values (in case of future changes or form bypass)
    for col in input_df.columns:
        min_val, max_val = feature_ranges[col]
        original = input_df[col].values[0]
        clipped = np.clip(original, min_val, max_val)
        if original != clipped:
            st.warning(f"⚠️ {col} value clipped from {original:.2f} to {clipped:.2f}")
        input_df[col] = clipped

    # Scale and predict
    scaled_input = scaler.transform(input_df)
    proba = model.predict_proba(scaled_input)[0][1]
    print(f"⚠️ Probability of Fault: {proba:.2f}")
    prediction = int(proba > 0.4)  # tune the thres

    # Display result
    if prediction == 1:
        st.error("❌ Fault Detected")
    else:
        st.success("✅ No Fault Detected")
