/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44VVI.c
 *
 * Code generated for Simulink model 'Group44VVI'.
 *
 * Model version                  : 1.2
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Mon Oct 17 16:30:25 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Group44VVI.h"
#include "rtwtypes.h"
#include <math.h>
#include "Group44VVI_types.h"

/* Named constants for Chart: '<S1>/Chart' */
#define Group44VVI_IN_AlertPeriod      ((uint8_T)1U)
#define Group44VVI_IN_PaceAtria        ((uint8_T)3U)
#define IN_ChargeC22_Atrial_DischargeC2 ((uint8_T)2U)

/* Block signals (default storage) */
B_Group44VVI_T Group44VVI_B;

/* Block states (default storage) */
DW_Group44VVI_T Group44VVI_DW;

/* Real-time model */
static RT_MODEL_Group44VVI_T Group44VVI_M_;
RT_MODEL_Group44VVI_T *const Group44VVI_M = &Group44VVI_M_;

/* Model step function */
void Group44VVI_step(void)
{
  boolean_T rtb_VENT_CMP_DETECT_0;

  /* MATLABSystem: '<Root>/VENT_CMP_DETECT' */
  if (Group44VVI_DW.obj.SampleTime != Group44VVI_P.VENT_CMP_DETECT_SampleTime) {
    Group44VVI_DW.obj.SampleTime = Group44VVI_P.VENT_CMP_DETECT_SampleTime;
  }

  rtb_VENT_CMP_DETECT_0 = MW_digitalIO_read
    (Group44VVI_DW.obj.MW_DIGITALIO_HANDLE);

  /* Chart: '<S1>/Chart' incorporates:
   *  Constant: '<Root>/p_VRP'
   *  Constant: '<Root>/p_lowrateInterval'
   *  Constant: '<Root>/p_vPaceAmp'
   *  Constant: '<Root>/p_vPaceWidth'
   *  Constant: '<Root>/p_vSensitivity'
   *  MATLABSystem: '<Root>/VENT_CMP_DETECT'
   */
  if (Group44VVI_DW.temporalCounter_i1 < MAX_uint32_T) {
    Group44VVI_DW.temporalCounter_i1++;
  }

  if (Group44VVI_DW.is_active_c3_Group44VVI == 0U) {
    Group44VVI_DW.is_active_c3_Group44VVI = 1U;
    Group44VVI_DW.is_c3_Group44VVI = IN_ChargeC22_Atrial_DischargeC2;
    Group44VVI_DW.temporalCounter_i1 = 0U;
    Group44VVI_B.ATR_PACE_CTRL = false;
    Group44VVI_B.VENT_PACE_CTRL = false;
    Group44VVI_B.PACE_CHARGE_CTRL = true;
    Group44VVI_B.PACE_GND_CTRL = true;
    Group44VVI_B.Z_ATR_CTRL = false;
    Group44VVI_B.Z_VENT_CTRL = false;
    Group44VVI_B.ATR_GND_CTRL = false;
    Group44VVI_B.VENT_GND_CTRL = true;
    Group44VVI_B.dutyCycle = Group44VVI_P.p_vPaceAmp_Value / 5.0 * 100.0;
    Group44VVI_B.senseDutyCycle = Group44VVI_P.p_vSensitivity_Value / 5.0 *
      100.0;
  } else {
    switch (Group44VVI_DW.is_c3_Group44VVI) {
     case Group44VVI_IN_AlertPeriod:
      if (Group44VVI_DW.temporalCounter_i1 >= (uint32_T)ceil
          ((Group44VVI_P.p_lowrateInterval_Value -
            Group44VVI_P.p_vPaceWidth_Value) - Group44VVI_P.p_VRP_Value)) {
        Group44VVI_DW.is_c3_Group44VVI = Group44VVI_IN_PaceAtria;
        Group44VVI_DW.temporalCounter_i1 = 0U;
        Group44VVI_B.PACE_CHARGE_CTRL = false;
        Group44VVI_B.PACE_GND_CTRL = true;
        Group44VVI_B.ATR_PACE_CTRL = false;
        Group44VVI_B.ATR_GND_CTRL = false;
        Group44VVI_B.Z_ATR_CTRL = false;
        Group44VVI_B.Z_VENT_CTRL = false;
        Group44VVI_B.VENT_GND_CTRL = false;
        Group44VVI_B.VENT_PACE_CTRL = true;
      } else if (rtb_VENT_CMP_DETECT_0) {
        Group44VVI_DW.is_c3_Group44VVI = IN_ChargeC22_Atrial_DischargeC2;
        Group44VVI_DW.temporalCounter_i1 = 0U;
        Group44VVI_B.ATR_PACE_CTRL = false;
        Group44VVI_B.VENT_PACE_CTRL = false;
        Group44VVI_B.PACE_CHARGE_CTRL = true;
        Group44VVI_B.PACE_GND_CTRL = true;
        Group44VVI_B.Z_ATR_CTRL = false;
        Group44VVI_B.Z_VENT_CTRL = false;
        Group44VVI_B.ATR_GND_CTRL = false;
        Group44VVI_B.VENT_GND_CTRL = true;
        Group44VVI_B.dutyCycle = Group44VVI_P.p_vPaceAmp_Value / 5.0 * 100.0;
        Group44VVI_B.senseDutyCycle = Group44VVI_P.p_vSensitivity_Value / 5.0 *
          100.0;
      }
      break;

     case IN_ChargeC22_Atrial_DischargeC2:
      Group44VVI_B.ATR_PACE_CTRL = false;
      Group44VVI_B.VENT_PACE_CTRL = false;
      Group44VVI_B.PACE_CHARGE_CTRL = true;
      Group44VVI_B.PACE_GND_CTRL = true;
      Group44VVI_B.Z_ATR_CTRL = false;
      Group44VVI_B.Z_VENT_CTRL = false;
      Group44VVI_B.ATR_GND_CTRL = false;
      Group44VVI_B.VENT_GND_CTRL = true;
      if (Group44VVI_DW.temporalCounter_i1 >= (uint32_T)ceil
          (Group44VVI_P.p_VRP_Value)) {
        Group44VVI_DW.is_c3_Group44VVI = Group44VVI_IN_AlertPeriod;
        Group44VVI_DW.temporalCounter_i1 = 0U;
      }
      break;

     default:
      /* case IN_PaceAtria: */
      Group44VVI_B.PACE_CHARGE_CTRL = false;
      Group44VVI_B.PACE_GND_CTRL = true;
      Group44VVI_B.ATR_PACE_CTRL = false;
      Group44VVI_B.ATR_GND_CTRL = false;
      Group44VVI_B.Z_ATR_CTRL = false;
      Group44VVI_B.Z_VENT_CTRL = false;
      Group44VVI_B.VENT_GND_CTRL = false;
      Group44VVI_B.VENT_PACE_CTRL = true;
      if (Group44VVI_DW.temporalCounter_i1 >= (uint32_T)ceil
          (Group44VVI_P.p_vPaceWidth_Value)) {
        Group44VVI_DW.is_c3_Group44VVI = IN_ChargeC22_Atrial_DischargeC2;
        Group44VVI_DW.temporalCounter_i1 = 0U;
        Group44VVI_B.VENT_PACE_CTRL = false;
        Group44VVI_B.PACE_CHARGE_CTRL = true;
        Group44VVI_B.VENT_GND_CTRL = true;
        Group44VVI_B.dutyCycle = Group44VVI_P.p_vPaceAmp_Value / 5.0 * 100.0;
        Group44VVI_B.senseDutyCycle = Group44VVI_P.p_vSensitivity_Value / 5.0 *
          100.0;
      }
      break;
    }
  }

  /* End of Chart: '<S1>/Chart' */

  /* MATLABSystem: '<Root>/ATR_GND_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_h5.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.ATR_GND_CTRL);

  /* MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_h.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.ATR_PACE_CTRL);

  /* MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_j.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.PACE_CHARGE_CTRL);

  /* MATLABSystem: '<Root>/PACE_GND_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_b.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.PACE_GND_CTRL);

  /* MATLABSystem: '<Root>/PACING_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44VVI_DW.obj_lh.MW_PWM_HANDLE, Group44VVI_B.dutyCycle);

  /* MATLABSystem: '<Root>/VENT_CMP_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44VVI_DW.obj_g.MW_PWM_HANDLE,
                      Group44VVI_B.senseDutyCycle);

  /* MATLABSystem: '<Root>/VENT_GND_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_l.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.VENT_GND_CTRL);

  /* MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_o.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.VENT_PACE_CTRL);

  /* MATLABSystem: '<Root>/Z_ATR_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_m.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.Z_ATR_CTRL);

  /* MATLABSystem: '<Root>/Z_VENT_CTRL' */
  MW_digitalIO_write(Group44VVI_DW.obj_c.MW_DIGITALIO_HANDLE,
                     Group44VVI_B.Z_VENT_CTRL);
}

/* Model initialize function */
void Group44VVI_initialize(void)
{
  {
    freedomk64f_DigitalRead_Group_T *obj;
    freedomk64f_DigitalWrite_Grou_T *obj_0;
    freedomk64f_PWMOutput_Group44_T *obj_1;

    /* Start for MATLABSystem: '<Root>/VENT_CMP_DETECT' */
    Group44VVI_DW.obj.matlabCodegenIsDeleted = false;
    Group44VVI_DW.obj.SampleTime = Group44VVI_P.VENT_CMP_DETECT_SampleTime;
    obj = &Group44VVI_DW.obj;
    Group44VVI_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(1U, 0);
    Group44VVI_DW.obj.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_GND_CTRL' */
    Group44VVI_DW.obj_h5.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_h5;
    Group44VVI_DW.obj_h5.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    Group44VVI_DW.obj_h5.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
    Group44VVI_DW.obj_h.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_h;
    Group44VVI_DW.obj_h.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    Group44VVI_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
    Group44VVI_DW.obj_j.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_j;
    Group44VVI_DW.obj_j.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    Group44VVI_DW.obj_j.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_GND_CTRL' */
    Group44VVI_DW.obj_b.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_b;
    Group44VVI_DW.obj_b.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    Group44VVI_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACING_REF_PWM' */
    Group44VVI_DW.obj_lh.matlabCodegenIsDeleted = false;
    obj_1 = &Group44VVI_DW.obj_lh;
    Group44VVI_DW.obj_lh.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(Group44VVI_DW.obj_lh.MW_PWM_HANDLE);
    Group44VVI_DW.obj_lh.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_CMP_REF_PWM' */
    Group44VVI_DW.obj_g.matlabCodegenIsDeleted = false;
    obj_1 = &Group44VVI_DW.obj_g;
    Group44VVI_DW.obj_g.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(3U, 2000.0, 0.0);
    MW_PWM_Start(Group44VVI_DW.obj_g.MW_PWM_HANDLE);
    Group44VVI_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_GND_CTRL' */
    Group44VVI_DW.obj_l.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_l;
    Group44VVI_DW.obj_l.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    Group44VVI_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
    Group44VVI_DW.obj_o.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_o;
    Group44VVI_DW.obj_o.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    Group44VVI_DW.obj_o.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_ATR_CTRL' */
    Group44VVI_DW.obj_m.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_m;
    Group44VVI_DW.obj_m.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    Group44VVI_DW.obj_m.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_VENT_CTRL' */
    Group44VVI_DW.obj_c.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VVI_DW.obj_c;
    Group44VVI_DW.obj_c.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    Group44VVI_DW.obj_c.isSetupComplete = true;
  }
}

/* Model terminate function */
void Group44VVI_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/VENT_CMP_DETECT' */
  if (!Group44VVI_DW.obj.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj.isInitialized == 1) &&
        Group44VVI_DW.obj.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_CMP_DETECT' */

  /* Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */
  if (!Group44VVI_DW.obj_h5.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_h5.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_h5.isInitialized == 1) &&
        Group44VVI_DW.obj_h5.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_h5.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  if (!Group44VVI_DW.obj_h.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_h.isInitialized == 1) &&
        Group44VVI_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  if (!Group44VVI_DW.obj_j.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_j.isInitialized == 1) &&
        Group44VVI_DW.obj_j.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_j.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */
  if (!Group44VVI_DW.obj_b.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_b.isInitialized == 1) &&
        Group44VVI_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */
  if (!Group44VVI_DW.obj_lh.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_lh.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_lh.isInitialized == 1) &&
        Group44VVI_DW.obj_lh.isSetupComplete) {
      MW_PWM_Stop(Group44VVI_DW.obj_lh.MW_PWM_HANDLE);
      MW_PWM_Close(Group44VVI_DW.obj_lh.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */

  /* Terminate for MATLABSystem: '<Root>/VENT_CMP_REF_PWM' */
  if (!Group44VVI_DW.obj_g.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_g.isInitialized == 1) &&
        Group44VVI_DW.obj_g.isSetupComplete) {
      MW_PWM_Stop(Group44VVI_DW.obj_g.MW_PWM_HANDLE);
      MW_PWM_Close(Group44VVI_DW.obj_g.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_CMP_REF_PWM' */

  /* Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */
  if (!Group44VVI_DW.obj_l.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_l.isInitialized == 1) &&
        Group44VVI_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  if (!Group44VVI_DW.obj_o.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_o.isInitialized == 1) &&
        Group44VVI_DW.obj_o.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_o.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */
  if (!Group44VVI_DW.obj_m.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_m.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_m.isInitialized == 1) &&
        Group44VVI_DW.obj_m.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_m.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
  if (!Group44VVI_DW.obj_c.matlabCodegenIsDeleted) {
    Group44VVI_DW.obj_c.matlabCodegenIsDeleted = true;
    if ((Group44VVI_DW.obj_c.isInitialized == 1) &&
        Group44VVI_DW.obj_c.isSetupComplete) {
      MW_digitalIO_close(Group44VVI_DW.obj_c.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
