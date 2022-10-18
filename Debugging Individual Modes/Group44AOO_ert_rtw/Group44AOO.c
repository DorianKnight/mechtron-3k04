/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44AOO.c
 *
 * Code generated for Simulink model 'Group44AOO'.
 *
 * Model version                  : 1.6
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Mon Oct 17 18:23:59 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Group44AOO.h"
#include "rtwtypes.h"
#include <math.h>
#include "Group44AOO_types.h"

/* Named constants for Chart: '<S1>/Chart' */
#define Group44AOO_IN_PaceAtria        ((uint8_T)2U)
#define IN_ChargeC22_Atrial_DischargeC2 ((uint8_T)1U)

/* Block signals (default storage) */
B_Group44AOO_T Group44AOO_B;

/* Block states (default storage) */
DW_Group44AOO_T Group44AOO_DW;

/* Real-time model */
static RT_MODEL_Group44AOO_T Group44AOO_M_;
RT_MODEL_Group44AOO_T *const Group44AOO_M = &Group44AOO_M_;

/* Model step function */
void Group44AOO_step(void)
{
  boolean_T rtb_ATR_GND_CTRL;
  boolean_T rtb_ATR_PACE_CTRL;
  boolean_T rtb_PACE_CHARGE_CTRL;

  /* Chart: '<S1>/Chart' incorporates:
   *  Constant: '<Root>/p_aPaceAmp'
   *  Constant: '<Root>/p_aPaceWidth'
   *  Constant: '<Root>/p_lowrateInterval'
   */
  if (Group44AOO_DW.temporalCounter_i1 < MAX_uint32_T) {
    Group44AOO_DW.temporalCounter_i1++;
  }

  if (Group44AOO_DW.is_active_c3_Group44AOO == 0U) {
    Group44AOO_DW.is_active_c3_Group44AOO = 1U;
    Group44AOO_DW.is_c3_Group44AOO = IN_ChargeC22_Atrial_DischargeC2;
    Group44AOO_DW.temporalCounter_i1 = 0U;
    rtb_ATR_PACE_CTRL = false;
    rtb_PACE_CHARGE_CTRL = true;
    rtb_ATR_GND_CTRL = true;
    Group44AOO_B.dutyCycle = Group44AOO_P.p_aPaceAmp_Value / 5.0 * 100.0;
  } else if (Group44AOO_DW.is_c3_Group44AOO == IN_ChargeC22_Atrial_DischargeC2)
  {
    rtb_ATR_PACE_CTRL = false;
    rtb_PACE_CHARGE_CTRL = true;
    rtb_ATR_GND_CTRL = true;
    if (Group44AOO_DW.temporalCounter_i1 >= (uint32_T)ceil
        (Group44AOO_P.p_lowrateInterval_Value - Group44AOO_P.p_aPaceWidth_Value))
    {
      Group44AOO_DW.is_c3_Group44AOO = Group44AOO_IN_PaceAtria;
      Group44AOO_DW.temporalCounter_i1 = 0U;
      rtb_PACE_CHARGE_CTRL = false;
      rtb_ATR_PACE_CTRL = true;
      rtb_ATR_GND_CTRL = false;
    }
  } else {
    /* case IN_PaceAtria: */
    rtb_PACE_CHARGE_CTRL = false;
    rtb_ATR_PACE_CTRL = true;
    rtb_ATR_GND_CTRL = false;
    if (Group44AOO_DW.temporalCounter_i1 >= (uint32_T)ceil
        (Group44AOO_P.p_aPaceWidth_Value)) {
      Group44AOO_DW.is_c3_Group44AOO = IN_ChargeC22_Atrial_DischargeC2;
      Group44AOO_DW.temporalCounter_i1 = 0U;
      rtb_ATR_PACE_CTRL = false;
      rtb_PACE_CHARGE_CTRL = true;
      rtb_ATR_GND_CTRL = true;
      Group44AOO_B.dutyCycle = Group44AOO_P.p_aPaceAmp_Value / 5.0 * 100.0;
    }
  }

  /* End of Chart: '<S1>/Chart' */

  /* MATLABSystem: '<Root>/ATR_GND_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_l5.MW_DIGITALIO_HANDLE, rtb_ATR_GND_CTRL);

  /* MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_e.MW_DIGITALIO_HANDLE, rtb_ATR_PACE_CTRL);

  /* MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_lf.MW_DIGITALIO_HANDLE,
                     rtb_PACE_CHARGE_CTRL);

  /* MATLABSystem: '<Root>/PACE_GND_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_h0.MW_DIGITALIO_HANDLE, true);

  /* MATLABSystem: '<Root>/PACING_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44AOO_DW.obj_b.MW_PWM_HANDLE, Group44AOO_B.dutyCycle);

  /* MATLABSystem: '<Root>/VENT_GND_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_h.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_g.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/Z_ATR_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj_l.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/Z_VENT_CTRL' */
  MW_digitalIO_write(Group44AOO_DW.obj.MW_DIGITALIO_HANDLE, false);
}

/* Model initialize function */
void Group44AOO_initialize(void)
{
  {
    freedomk64f_DigitalWrite_Grou_T *obj;
    freedomk64f_PWMOutput_Group44_T *obj_0;

    /* Start for MATLABSystem: '<Root>/ATR_GND_CTRL' */
    Group44AOO_DW.obj_l5.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_l5;
    Group44AOO_DW.obj_l5.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    Group44AOO_DW.obj_l5.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
    Group44AOO_DW.obj_e.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_e;
    Group44AOO_DW.obj_e.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    Group44AOO_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
    Group44AOO_DW.obj_lf.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_lf;
    Group44AOO_DW.obj_lf.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    Group44AOO_DW.obj_lf.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_GND_CTRL' */
    Group44AOO_DW.obj_h0.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_h0;
    Group44AOO_DW.obj_h0.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    Group44AOO_DW.obj_h0.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACING_REF_PWM' */
    Group44AOO_DW.obj_b.matlabCodegenIsDeleted = false;
    obj_0 = &Group44AOO_DW.obj_b;
    Group44AOO_DW.obj_b.isInitialized = 1;
    obj_0->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(Group44AOO_DW.obj_b.MW_PWM_HANDLE);
    Group44AOO_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_GND_CTRL' */
    Group44AOO_DW.obj_h.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_h;
    Group44AOO_DW.obj_h.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    Group44AOO_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
    Group44AOO_DW.obj_g.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_g;
    Group44AOO_DW.obj_g.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    Group44AOO_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_ATR_CTRL' */
    Group44AOO_DW.obj_l.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj_l;
    Group44AOO_DW.obj_l.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    Group44AOO_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_VENT_CTRL' */
    Group44AOO_DW.obj.matlabCodegenIsDeleted = false;
    obj = &Group44AOO_DW.obj;
    Group44AOO_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    Group44AOO_DW.obj.isSetupComplete = true;
  }
}

/* Model terminate function */
void Group44AOO_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */
  if (!Group44AOO_DW.obj_l5.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_l5.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_l5.isInitialized == 1) &&
        Group44AOO_DW.obj_l5.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_l5.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  if (!Group44AOO_DW.obj_e.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_e.isInitialized == 1) &&
        Group44AOO_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  if (!Group44AOO_DW.obj_lf.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_lf.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_lf.isInitialized == 1) &&
        Group44AOO_DW.obj_lf.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_lf.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */
  if (!Group44AOO_DW.obj_h0.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_h0.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_h0.isInitialized == 1) &&
        Group44AOO_DW.obj_h0.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_h0.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */
  if (!Group44AOO_DW.obj_b.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_b.isInitialized == 1) &&
        Group44AOO_DW.obj_b.isSetupComplete) {
      MW_PWM_Stop(Group44AOO_DW.obj_b.MW_PWM_HANDLE);
      MW_PWM_Close(Group44AOO_DW.obj_b.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */

  /* Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */
  if (!Group44AOO_DW.obj_h.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_h.isInitialized == 1) &&
        Group44AOO_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  if (!Group44AOO_DW.obj_g.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_g.isInitialized == 1) &&
        Group44AOO_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */
  if (!Group44AOO_DW.obj_l.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj_l.isInitialized == 1) &&
        Group44AOO_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
  if (!Group44AOO_DW.obj.matlabCodegenIsDeleted) {
    Group44AOO_DW.obj.matlabCodegenIsDeleted = true;
    if ((Group44AOO_DW.obj.isInitialized == 1) &&
        Group44AOO_DW.obj.isSetupComplete) {
      MW_digitalIO_close(Group44AOO_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
