/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44VOOAcutal.c
 *
 * Code generated for Simulink model 'Group44VOOAcutal'.
 *
 * Model version                  : 1.9
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Mon Oct 17 18:33:36 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Group44VOOAcutal.h"
#include "rtwtypes.h"
#include <math.h>
#include "Group44VOOAcutal_types.h"

/* Named constants for Chart: '<S1>/Chart' */
#define Group44VOOAcutal_IN_PaceAtria  ((uint8_T)2U)
#define IN_ChargeC22_Atrial_DischargeC2 ((uint8_T)1U)

/* Block signals (default storage) */
B_Group44VOOAcutal_T Group44VOOAcutal_B;

/* Block states (default storage) */
DW_Group44VOOAcutal_T Group44VOOAcutal_DW;

/* Real-time model */
static RT_MODEL_Group44VOOAcutal_T Group44VOOAcutal_M_;
RT_MODEL_Group44VOOAcutal_T *const Group44VOOAcutal_M = &Group44VOOAcutal_M_;

/* Model step function */
void Group44VOOAcutal_step(void)
{
  boolean_T rtb_PACE_CHARGE_CTRL;
  boolean_T rtb_VENT_GND_CTRL;
  boolean_T rtb_VENT_PACE_CTRL;

  /* Chart: '<S1>/Chart' incorporates:
   *  Constant: '<Root>/p_lowrateInterval'
   *  Constant: '<Root>/p_vPaceAmp'
   *  Constant: '<Root>/p_vPaceWidth'
   */
  if (Group44VOOAcutal_DW.temporalCounter_i1 < MAX_uint32_T) {
    Group44VOOAcutal_DW.temporalCounter_i1++;
  }

  if (Group44VOOAcutal_DW.is_active_c3_Group44VOOAcutal == 0U) {
    Group44VOOAcutal_DW.is_active_c3_Group44VOOAcutal = 1U;
    Group44VOOAcutal_DW.is_c3_Group44VOOAcutal = IN_ChargeC22_Atrial_DischargeC2;
    Group44VOOAcutal_DW.temporalCounter_i1 = 0U;
    rtb_VENT_PACE_CTRL = false;
    rtb_VENT_GND_CTRL = true;
    rtb_PACE_CHARGE_CTRL = true;
    Group44VOOAcutal_B.dutyCycle = Group44VOOAcutal_P.p_vPaceAmp_Value / 5.0 *
      100.0;
  } else if (Group44VOOAcutal_DW.is_c3_Group44VOOAcutal ==
             IN_ChargeC22_Atrial_DischargeC2) {
    rtb_VENT_PACE_CTRL = false;
    rtb_VENT_GND_CTRL = true;
    rtb_PACE_CHARGE_CTRL = true;
    if (Group44VOOAcutal_DW.temporalCounter_i1 >= (uint32_T)ceil
        (Group44VOOAcutal_P.p_lowrateInterval_Value -
         Group44VOOAcutal_P.p_vPaceWidth_Value)) {
      Group44VOOAcutal_DW.is_c3_Group44VOOAcutal = Group44VOOAcutal_IN_PaceAtria;
      Group44VOOAcutal_DW.temporalCounter_i1 = 0U;
      rtb_PACE_CHARGE_CTRL = false;
      rtb_VENT_GND_CTRL = false;
      rtb_VENT_PACE_CTRL = true;
    }
  } else {
    /* case IN_PaceAtria: */
    rtb_PACE_CHARGE_CTRL = false;
    rtb_VENT_GND_CTRL = false;
    rtb_VENT_PACE_CTRL = true;
    if (Group44VOOAcutal_DW.temporalCounter_i1 >= (uint32_T)ceil
        (Group44VOOAcutal_P.p_vPaceWidth_Value)) {
      Group44VOOAcutal_DW.is_c3_Group44VOOAcutal =
        IN_ChargeC22_Atrial_DischargeC2;
      Group44VOOAcutal_DW.temporalCounter_i1 = 0U;
      rtb_VENT_PACE_CTRL = false;
      rtb_VENT_GND_CTRL = true;
      rtb_PACE_CHARGE_CTRL = true;
      Group44VOOAcutal_B.dutyCycle = Group44VOOAcutal_P.p_vPaceAmp_Value / 5.0 *
        100.0;
    }
  }

  /* End of Chart: '<S1>/Chart' */

  /* MATLABSystem: '<Root>/ATR_GND_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_o.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_m.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_c.MW_DIGITALIO_HANDLE,
                     rtb_PACE_CHARGE_CTRL);

  /* MATLABSystem: '<Root>/PACE_GND_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_k.MW_DIGITALIO_HANDLE, true);

  /* MATLABSystem: '<Root>/PACING_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44VOOAcutal_DW.obj_p.MW_PWM_HANDLE,
                      Group44VOOAcutal_B.dutyCycle);

  /* MATLABSystem: '<Root>/VENT_GND_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_gy.MW_DIGITALIO_HANDLE,
                     rtb_VENT_GND_CTRL);

  /* MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_e.MW_DIGITALIO_HANDLE,
                     rtb_VENT_PACE_CTRL);

  /* MATLABSystem: '<Root>/Z_ATR_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj_g.MW_DIGITALIO_HANDLE, false);

  /* MATLABSystem: '<Root>/Z_VENT_CTRL' */
  MW_digitalIO_write(Group44VOOAcutal_DW.obj.MW_DIGITALIO_HANDLE, false);
}

/* Model initialize function */
void Group44VOOAcutal_initialize(void)
{
  {
    freedomk64f_DigitalWrite_Grou_T *obj;
    freedomk64f_PWMOutput_Group44_T *obj_0;

    /* Start for MATLABSystem: '<Root>/ATR_GND_CTRL' */
    Group44VOOAcutal_DW.obj_o.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_o;
    Group44VOOAcutal_DW.obj_o.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    Group44VOOAcutal_DW.obj_o.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
    Group44VOOAcutal_DW.obj_m.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_m;
    Group44VOOAcutal_DW.obj_m.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    Group44VOOAcutal_DW.obj_m.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
    Group44VOOAcutal_DW.obj_c.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_c;
    Group44VOOAcutal_DW.obj_c.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    Group44VOOAcutal_DW.obj_c.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_GND_CTRL' */
    Group44VOOAcutal_DW.obj_k.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_k;
    Group44VOOAcutal_DW.obj_k.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    Group44VOOAcutal_DW.obj_k.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACING_REF_PWM' */
    Group44VOOAcutal_DW.obj_p.matlabCodegenIsDeleted = false;
    obj_0 = &Group44VOOAcutal_DW.obj_p;
    Group44VOOAcutal_DW.obj_p.isInitialized = 1;
    obj_0->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(Group44VOOAcutal_DW.obj_p.MW_PWM_HANDLE);
    Group44VOOAcutal_DW.obj_p.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_GND_CTRL' */
    Group44VOOAcutal_DW.obj_gy.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_gy;
    Group44VOOAcutal_DW.obj_gy.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    Group44VOOAcutal_DW.obj_gy.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
    Group44VOOAcutal_DW.obj_e.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_e;
    Group44VOOAcutal_DW.obj_e.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    Group44VOOAcutal_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_ATR_CTRL' */
    Group44VOOAcutal_DW.obj_g.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj_g;
    Group44VOOAcutal_DW.obj_g.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    Group44VOOAcutal_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_VENT_CTRL' */
    Group44VOOAcutal_DW.obj.matlabCodegenIsDeleted = false;
    obj = &Group44VOOAcutal_DW.obj;
    Group44VOOAcutal_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    Group44VOOAcutal_DW.obj.isSetupComplete = true;
  }
}

/* Model terminate function */
void Group44VOOAcutal_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */
  if (!Group44VOOAcutal_DW.obj_o.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_o.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_o.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_o.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  if (!Group44VOOAcutal_DW.obj_m.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_m.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_m.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_m.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_m.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  if (!Group44VOOAcutal_DW.obj_c.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_c.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_c.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_c.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_c.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */
  if (!Group44VOOAcutal_DW.obj_k.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_k.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_k.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_k.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_k.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */
  if (!Group44VOOAcutal_DW.obj_p.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_p.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_p.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_p.isSetupComplete) {
      MW_PWM_Stop(Group44VOOAcutal_DW.obj_p.MW_PWM_HANDLE);
      MW_PWM_Close(Group44VOOAcutal_DW.obj_p.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */

  /* Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */
  if (!Group44VOOAcutal_DW.obj_gy.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_gy.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_gy.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_gy.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_gy.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  if (!Group44VOOAcutal_DW.obj_e.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_e.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */
  if (!Group44VOOAcutal_DW.obj_g.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj_g.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
  if (!Group44VOOAcutal_DW.obj.matlabCodegenIsDeleted) {
    Group44VOOAcutal_DW.obj.matlabCodegenIsDeleted = true;
    if ((Group44VOOAcutal_DW.obj.isInitialized == 1) &&
        Group44VOOAcutal_DW.obj.isSetupComplete) {
      MW_digitalIO_close(Group44VOOAcutal_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_VENT_CTRL' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
