/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44PACEMAKER.c
 *
 * Code generated for Simulink model 'Group44PACEMAKER'.
 *
 * Model version                  : 1.119
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Tue Oct 18 13:09:07 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Group44PACEMAKER.h"
#include "rtwtypes.h"
#include <string.h>
#include <math.h>
#include "Group44PACEMAKER_types.h"

/* Named constants for Chart: '<S4>/Chart' */
#define Group44PACEMAKER_IN_PaceAtria  ((uint8_T)5U)
#define Group44PACEMAK_IN_PaceVentricle ((uint8_T)6U)
#define Group44PAC_IN_AtrialAlertPeriod ((uint8_T)1U)
#define Group_IN_Default_Starting_State ((uint8_T)4U)
#define Group_IN_VentricularAlertPeriod ((uint8_T)7U)
#define IN_ChargeC22_Atrial_DischargeC2 ((uint8_T)2U)
#define IN_ChargeC22_Ventricular_Discha ((uint8_T)3U)

/* Block signals (default storage) */
B_Group44PACEMAKER_T Group44PACEMAKER_B;

/* Block states (default storage) */
DW_Group44PACEMAKER_T Group44PACEMAKER_DW;

/* Real-time model */
static RT_MODEL_Group44PACEMAKER_T Group44PACEMAKER_M_;
RT_MODEL_Group44PACEMAKER_T *const Group44PACEMAKER_M = &Group44PACEMAKER_M_;

/* Forward declaration for local functions */
static void Group44P_VentricularAlertPeriod(const boolean_T *in_VENT_CMP_DETECT);
static void Group44P_Default_Starting_State(const char_T mode[256]);

/* Function for Chart: '<S4>/Chart' */
static void Group44P_VentricularAlertPeriod(const boolean_T *in_VENT_CMP_DETECT)
{
  real_T tmp;
  if (*in_VENT_CMP_DETECT) {
    Group44PACEMAKER_DW.natPaceDetected = true;
    Group44PACEMAKER_DW.is_c6_Group44PACEMAKER = IN_ChargeC22_Ventricular_Discha;
    Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
    Group44PACEMAKER_B.ATR_PACE_CTRL = false;
    Group44PACEMAKER_B.VENT_PACE_CTRL = false;
    Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
    Group44PACEMAKER_B.PACE_GND_CTRL = true;
    Group44PACEMAKER_B.Z_ATR_CTRL = false;
    Group44PACEMAKER_B.Z_VENT_CTRL = false;
    Group44PACEMAKER_B.ATR_GND_CTRL = false;
    Group44PACEMAKER_B.VENT_GND_CTRL = true;
  } else {
    /* Constant: '<S2>/in_p_lowrateInterval' incorporates:
     *  Constant: '<S2>/in_p_VRP'
     *  Constant: '<S2>/in_p_vPaceWidth'
     */
    tmp = (Group44PACEMAKER_P.in_p_lowrateInterval_Value -
           Group44PACEMAKER_P.in_p_VRP_Value) -
      Group44PACEMAKER_P.in_p_vPaceWidth_Value;

    /* Constant: '<S2>/in_p_hysteresisInterval' incorporates:
     *  Constant: '<S2>/in_p_hysteresis'
     */
    if (((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil(tmp +
           Group44PACEMAKER_P.in_p_hysteresisInterval_Value)) &&
         (Group44PACEMAKER_P.in_p_hysteresis_Value &&
          Group44PACEMAKER_DW.natPaceDetected)) ||
        ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil(tmp)) &&
         ((!Group44PACEMAKER_P.in_p_hysteresis_Value) ||
          (Group44PACEMAKER_P.in_p_hysteresis_Value &&
           (!Group44PACEMAKER_DW.natPaceDetected))))) {
      Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
        Group44PACEMAK_IN_PaceVentricle;
      Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
      Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
      Group44PACEMAKER_B.PACE_GND_CTRL = true;
      Group44PACEMAKER_B.ATR_PACE_CTRL = false;
      Group44PACEMAKER_B.ATR_GND_CTRL = false;
      Group44PACEMAKER_B.Z_ATR_CTRL = false;
      Group44PACEMAKER_B.Z_VENT_CTRL = false;
      Group44PACEMAKER_B.VENT_GND_CTRL = false;
      Group44PACEMAKER_B.VENT_PACE_CTRL = true;
      Group44PACEMAKER_DW.natPaceDetected = false;
    }

    /* End of Constant: '<S2>/in_p_hysteresisInterval' */
  }
}

/* Function for Chart: '<S4>/Chart' */
static void Group44P_Default_Starting_State(const char_T mode[256])
{
  boolean_T guard1 = false;
  boolean_T guard2 = false;
  boolean_T guard3 = false;

  /* Constant: '<S2>/in_p_aPaceWidth' */
  guard1 = false;
  guard2 = false;
  guard3 = false;
  if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
       (Group44PACEMAKER_P.in_p_aPaceWidth_Value)) && ((strcmp(&mode[0], "AOO") ==
        0) || (strcmp(&mode[0], "AAI") == 0))) {
    /* Constant: '<S2>/in_p_aPaceAmp' */
    Group44PACEMAKER_B.dutyCycle = Group44PACEMAKER_P.in_p_aPaceAmp_Value / 5.0 *
      100.0;
    if (strcmp(&mode[0], "AOO") == 0) {
      guard1 = true;
    } else if (strcmp(&mode[0], "AAI") == 0) {
      /* Constant: '<S2>/in_p_aSensitivity' */
      Group44PACEMAKER_B.cmpDutyCycle =
        Group44PACEMAKER_P.in_p_aSensitivity_Value / 5.0 * 100.0;
      guard1 = true;
    } else {
      guard3 = true;
    }
  } else {
    guard3 = true;
  }

  if (guard3) {
    if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
         (Group44PACEMAKER_P.in_p_vPaceWidth_Value)) && ((strcmp(&mode[0], "VOO")
          == 0) || (strcmp(&mode[0], "VVI") == 0))) {
      /* Constant: '<S2>/in_p_vPaceAmp' */
      Group44PACEMAKER_B.dutyCycle = Group44PACEMAKER_P.in_p_vPaceAmp_Value /
        5.0 * 100.0;
      if (strcmp(&mode[0], "VOO") == 0) {
        guard2 = true;
      } else if (strcmp(&mode[0], "VVI") == 0) {
        /* Constant: '<S2>/in_p_vSensitivity' */
        Group44PACEMAKER_B.cmpDutyCycle =
          Group44PACEMAKER_P.in_p_vSensitivity_Value / 5.0 * 100.0;
        guard2 = true;
      } else {
        Group44PACEMAKER_DW.natPaceDetected = false;
      }
    } else {
      Group44PACEMAKER_DW.natPaceDetected = false;
    }
  }

  if (guard2) {
    Group44PACEMAKER_DW.is_c6_Group44PACEMAKER = IN_ChargeC22_Ventricular_Discha;
    Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
    Group44PACEMAKER_B.ATR_PACE_CTRL = false;
    Group44PACEMAKER_B.VENT_PACE_CTRL = false;
    Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
    Group44PACEMAKER_B.PACE_GND_CTRL = true;
    Group44PACEMAKER_B.Z_ATR_CTRL = false;
    Group44PACEMAKER_B.Z_VENT_CTRL = false;
    Group44PACEMAKER_B.ATR_GND_CTRL = false;
    Group44PACEMAKER_B.VENT_GND_CTRL = true;
  }

  if (guard1) {
    Group44PACEMAKER_DW.is_c6_Group44PACEMAKER = IN_ChargeC22_Atrial_DischargeC2;
    Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
    Group44PACEMAKER_B.ATR_PACE_CTRL = false;
    Group44PACEMAKER_B.VENT_PACE_CTRL = false;
    Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
    Group44PACEMAKER_B.PACE_GND_CTRL = true;
    Group44PACEMAKER_B.Z_ATR_CTRL = false;
    Group44PACEMAKER_B.Z_VENT_CTRL = false;
    Group44PACEMAKER_B.ATR_GND_CTRL = true;
    Group44PACEMAKER_B.VENT_GND_CTRL = false;
  }

  /* End of Constant: '<S2>/in_p_aPaceWidth' */
}

/* Model step function */
void Group44PACEMAKER_step(void)
{
  real_T tmp_0;
  uint32_T tmp_1;
  boolean_T in_VENT_CMP_DETECT;
  boolean_T tmp;

  /* MATLABSystem: '<S1>/in_ATR_CMP_DETECT' */
  if (Group44PACEMAKER_DW.obj_c.SampleTime !=
      Group44PACEMAKER_P.in_ATR_CMP_DETECT_SampleTime) {
    Group44PACEMAKER_DW.obj_c.SampleTime =
      Group44PACEMAKER_P.in_ATR_CMP_DETECT_SampleTime;
  }

  tmp = MW_digitalIO_read(Group44PACEMAKER_DW.obj_c.MW_DIGITALIO_HANDLE);

  /* End of MATLABSystem: '<S1>/in_ATR_CMP_DETECT' */

  /* MATLABSystem: '<S1>/in_VENT_CMP_DETECT' */
  if (Group44PACEMAKER_DW.obj.SampleTime !=
      Group44PACEMAKER_P.in_VENT_CMP_DETECT_SampleTime) {
    Group44PACEMAKER_DW.obj.SampleTime =
      Group44PACEMAKER_P.in_VENT_CMP_DETECT_SampleTime;
  }

  /* MATLABSystem: '<S1>/in_VENT_CMP_DETECT' */
  in_VENT_CMP_DETECT = MW_digitalIO_read
    (Group44PACEMAKER_DW.obj.MW_DIGITALIO_HANDLE);

  /* StringConstant: '<S2>/mode' */
  strncpy(&Group44PACEMAKER_B.mode[0], &Group44PACEMAKER_P.mode_String[0], 255U);
  Group44PACEMAKER_B.mode[255] = '\x00';

  /* Chart: '<S4>/Chart' incorporates:
   *  Constant: '<S2>/in_p_ARP'
   *  Constant: '<S2>/in_p_VRP'
   *  Constant: '<S2>/in_p_aPaceWidth'
   *  Constant: '<S2>/in_p_lowrateInterval'
   *  Constant: '<S2>/in_p_vPaceWidth'
   *  StringConstant: '<S2>/mode'
   */
  if (Group44PACEMAKER_DW.temporalCounter_i1 < MAX_uint32_T) {
    Group44PACEMAKER_DW.temporalCounter_i1++;
  }

  if (Group44PACEMAKER_DW.is_active_c6_Group44PACEMAKER == 0U) {
    Group44PACEMAKER_DW.is_active_c6_Group44PACEMAKER = 1U;
    Group44PACEMAKER_DW.is_c6_Group44PACEMAKER = Group_IN_Default_Starting_State;
    Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
    Group44PACEMAKER_DW.natPaceDetected = false;
  } else {
    switch (Group44PACEMAKER_DW.is_c6_Group44PACEMAKER) {
     case Group44PAC_IN_AtrialAlertPeriod:
      if (tmp) {
        Group44PACEMAKER_DW.natPaceDetected = true;
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          IN_ChargeC22_Atrial_DischargeC2;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
        Group44PACEMAKER_B.ATR_PACE_CTRL = false;
        Group44PACEMAKER_B.VENT_PACE_CTRL = false;
        Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
        Group44PACEMAKER_B.PACE_GND_CTRL = true;
        Group44PACEMAKER_B.Z_ATR_CTRL = false;
        Group44PACEMAKER_B.Z_VENT_CTRL = false;
        Group44PACEMAKER_B.ATR_GND_CTRL = true;
        Group44PACEMAKER_B.VENT_GND_CTRL = false;
      } else {
        tmp_0 = (Group44PACEMAKER_P.in_p_lowrateInterval_Value -
                 Group44PACEMAKER_P.in_p_ARP_Value) -
          Group44PACEMAKER_P.in_p_aPaceWidth_Value;
        if (((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil(tmp_0)) &&
             ((!Group44PACEMAKER_P.in_p_hysteresis_Value) ||
              ((!Group44PACEMAKER_DW.natPaceDetected) &&
               Group44PACEMAKER_P.in_p_hysteresis_Value))) ||
            ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil(tmp_0 +
               Group44PACEMAKER_P.in_p_hysteresisInterval_Value)) &&
             (Group44PACEMAKER_P.in_p_hysteresis_Value &&
              Group44PACEMAKER_DW.natPaceDetected))) {
          Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
            Group44PACEMAKER_IN_PaceAtria;
          Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
          Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
          Group44PACEMAKER_B.PACE_GND_CTRL = true;
          Group44PACEMAKER_B.ATR_PACE_CTRL = true;
          Group44PACEMAKER_B.ATR_GND_CTRL = false;
          Group44PACEMAKER_B.Z_ATR_CTRL = false;
          Group44PACEMAKER_B.Z_VENT_CTRL = false;
          Group44PACEMAKER_B.VENT_GND_CTRL = false;
          Group44PACEMAKER_B.VENT_PACE_CTRL = false;
        }
      }
      break;

     case IN_ChargeC22_Atrial_DischargeC2:
      Group44PACEMAKER_B.ATR_PACE_CTRL = false;
      Group44PACEMAKER_B.VENT_PACE_CTRL = false;
      Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
      Group44PACEMAKER_B.PACE_GND_CTRL = true;
      Group44PACEMAKER_B.Z_ATR_CTRL = false;
      Group44PACEMAKER_B.Z_VENT_CTRL = false;
      Group44PACEMAKER_B.ATR_GND_CTRL = true;
      Group44PACEMAKER_B.VENT_GND_CTRL = false;
      if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
           (Group44PACEMAKER_P.in_p_lowrateInterval_Value -
            Group44PACEMAKER_P.in_p_aPaceWidth_Value)) && (strcmp
           (&Group44PACEMAKER_P.mode_String[0], "AOO") == 0)) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          Group44PACEMAKER_IN_PaceAtria;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
        Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
        Group44PACEMAKER_B.ATR_PACE_CTRL = true;
        Group44PACEMAKER_B.ATR_GND_CTRL = false;
      } else if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
                  (Group44PACEMAKER_P.in_p_ARP_Value)) && (strcmp
                  (&Group44PACEMAKER_P.mode_String[0], "AAI") == 0)) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          Group44PAC_IN_AtrialAlertPeriod;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
      }
      break;

     case IN_ChargeC22_Ventricular_Discha:
      Group44PACEMAKER_B.ATR_PACE_CTRL = false;
      Group44PACEMAKER_B.VENT_PACE_CTRL = false;
      Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
      Group44PACEMAKER_B.PACE_GND_CTRL = true;
      Group44PACEMAKER_B.Z_ATR_CTRL = false;
      Group44PACEMAKER_B.Z_VENT_CTRL = false;
      Group44PACEMAKER_B.ATR_GND_CTRL = false;
      Group44PACEMAKER_B.VENT_GND_CTRL = true;
      if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
           (Group44PACEMAKER_P.in_p_lowrateInterval_Value -
            Group44PACEMAKER_P.in_p_vPaceWidth_Value)) && (strcmp
           (&Group44PACEMAKER_P.mode_String[0], "VOO") == 0)) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          Group44PACEMAK_IN_PaceVentricle;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
        Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
        Group44PACEMAKER_B.VENT_GND_CTRL = false;
        Group44PACEMAKER_B.VENT_PACE_CTRL = true;
        Group44PACEMAKER_DW.natPaceDetected = false;
      } else if ((Group44PACEMAKER_DW.temporalCounter_i1 >= (uint32_T)ceil
                  (Group44PACEMAKER_P.in_p_VRP_Value)) && (strcmp
                  (&Group44PACEMAKER_P.mode_String[0], "VVI") == 0)) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          Group_IN_VentricularAlertPeriod;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
      }
      break;

     case Group_IN_Default_Starting_State:
      Group44P_Default_Starting_State(Group44PACEMAKER_B.mode);
      break;

     case Group44PACEMAKER_IN_PaceAtria:
      Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
      Group44PACEMAKER_B.PACE_GND_CTRL = true;
      Group44PACEMAKER_B.ATR_PACE_CTRL = true;
      Group44PACEMAKER_B.ATR_GND_CTRL = false;
      Group44PACEMAKER_B.Z_ATR_CTRL = false;
      Group44PACEMAKER_B.Z_VENT_CTRL = false;
      Group44PACEMAKER_B.VENT_GND_CTRL = false;
      Group44PACEMAKER_B.VENT_PACE_CTRL = false;
      tmp_1 = (uint32_T)ceil(Group44PACEMAKER_P.in_p_aPaceWidth_Value);
      if (((Group44PACEMAKER_DW.temporalCounter_i1 >= tmp_1) && (strcmp
            (&Group44PACEMAKER_P.mode_String[0], "AOO") == 0)) ||
          ((Group44PACEMAKER_DW.temporalCounter_i1 >= tmp_1) && (strcmp
            (&Group44PACEMAKER_P.mode_String[0], "AAI") == 0))) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          IN_ChargeC22_Atrial_DischargeC2;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
        Group44PACEMAKER_B.ATR_PACE_CTRL = false;
        Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
        Group44PACEMAKER_B.ATR_GND_CTRL = true;
      }
      break;

     case Group44PACEMAK_IN_PaceVentricle:
      Group44PACEMAKER_B.PACE_CHARGE_CTRL = false;
      Group44PACEMAKER_B.PACE_GND_CTRL = true;
      Group44PACEMAKER_B.ATR_PACE_CTRL = false;
      Group44PACEMAKER_B.ATR_GND_CTRL = false;
      Group44PACEMAKER_B.Z_ATR_CTRL = false;
      Group44PACEMAKER_B.Z_VENT_CTRL = false;
      Group44PACEMAKER_B.VENT_GND_CTRL = false;
      Group44PACEMAKER_B.VENT_PACE_CTRL = true;
      tmp_1 = (uint32_T)ceil(Group44PACEMAKER_P.in_p_vPaceWidth_Value);
      if (((Group44PACEMAKER_DW.temporalCounter_i1 >= tmp_1) && (strcmp
            (&Group44PACEMAKER_P.mode_String[0], "VOO") == 0)) ||
          ((Group44PACEMAKER_DW.temporalCounter_i1 >= tmp_1) && (strcmp
            (&Group44PACEMAKER_P.mode_String[0], "VVI") == 0))) {
        Group44PACEMAKER_DW.is_c6_Group44PACEMAKER =
          IN_ChargeC22_Ventricular_Discha;
        Group44PACEMAKER_DW.temporalCounter_i1 = 0U;
        Group44PACEMAKER_B.VENT_PACE_CTRL = false;
        Group44PACEMAKER_B.PACE_CHARGE_CTRL = true;
        Group44PACEMAKER_B.VENT_GND_CTRL = true;
      }
      break;

     default:
      /* case IN_VentricularAlertPeriod: */
      Group44P_VentricularAlertPeriod(&in_VENT_CMP_DETECT);
      break;
    }
  }

  /* End of Chart: '<S4>/Chart' */

  /* MATLABSystem: '<S3>/OUT_ATR_GND_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_i.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.ATR_GND_CTRL);

  /* MATLABSystem: '<S3>/OUT_ATR_PACE_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_d2.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.ATR_PACE_CTRL);

  /* MATLABSystem: '<S3>/OUT_Z_ATR_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_n.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.Z_ATR_CTRL);

  /* MATLABSystem: '<S3>/OUT_PACE_CHARGE_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_b.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.PACE_CHARGE_CTRL);

  /* MATLABSystem: '<S3>/OUT_PACE_GND_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_o.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.PACE_GND_CTRL);

  /* MATLABSystem: '<S3>/OUT_Z_VENT_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_d.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.Z_VENT_CTRL);

  /* MATLABSystem: '<S3>/OUT_VENT_GND_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_l.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.VENT_GND_CTRL);

  /* MATLABSystem: '<S3>/OUT_VENT_PACE_CTRL' */
  MW_digitalIO_write(Group44PACEMAKER_DW.obj_e.MW_DIGITALIO_HANDLE,
                     Group44PACEMAKER_B.VENT_PACE_CTRL);

  /* MATLABSystem: '<S3>/OUT_PACING_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44PACEMAKER_DW.obj_m.MW_PWM_HANDLE,
                      Group44PACEMAKER_B.dutyCycle);

  /* MATLABSystem: '<S3>/OUT_VENT_CMP_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44PACEMAKER_DW.obj_j.MW_PWM_HANDLE,
                      Group44PACEMAKER_B.cmpDutyCycle);

  /* MATLABSystem: '<S3>/OUT_ATR_CMP_REF_PWM' */
  MW_PWM_SetDutyCycle(Group44PACEMAKER_DW.obj_c2.MW_PWM_HANDLE,
                      Group44PACEMAKER_B.cmpDutyCycle);
}

/* Model initialize function */
void Group44PACEMAKER_initialize(void)
{
  {
    freedomk64f_DigitalRead_Group_T *obj;
    freedomk64f_DigitalWrite_Grou_T *obj_0;
    freedomk64f_PWMOutput_Group44_T *obj_1;

    /* Start for MATLABSystem: '<S1>/in_ATR_CMP_DETECT' */
    Group44PACEMAKER_DW.obj_c.matlabCodegenIsDeleted = false;
    Group44PACEMAKER_DW.obj_c.SampleTime =
      Group44PACEMAKER_P.in_ATR_CMP_DETECT_SampleTime;
    obj = &Group44PACEMAKER_DW.obj_c;
    Group44PACEMAKER_DW.obj_c.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(0U, 0);
    Group44PACEMAKER_DW.obj_c.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/in_VENT_CMP_DETECT' */
    Group44PACEMAKER_DW.obj.matlabCodegenIsDeleted = false;
    Group44PACEMAKER_DW.obj.SampleTime =
      Group44PACEMAKER_P.in_VENT_CMP_DETECT_SampleTime;
    obj = &Group44PACEMAKER_DW.obj;
    Group44PACEMAKER_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(1U, 0);
    Group44PACEMAKER_DW.obj.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_ATR_GND_CTRL' */
    Group44PACEMAKER_DW.obj_i.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_i;
    Group44PACEMAKER_DW.obj_i.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    Group44PACEMAKER_DW.obj_i.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_ATR_PACE_CTRL' */
    Group44PACEMAKER_DW.obj_d2.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_d2;
    Group44PACEMAKER_DW.obj_d2.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    Group44PACEMAKER_DW.obj_d2.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_Z_ATR_CTRL' */
    Group44PACEMAKER_DW.obj_n.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_n;
    Group44PACEMAKER_DW.obj_n.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    Group44PACEMAKER_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_PACE_CHARGE_CTRL' */
    Group44PACEMAKER_DW.obj_b.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_b;
    Group44PACEMAKER_DW.obj_b.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    Group44PACEMAKER_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_PACE_GND_CTRL' */
    Group44PACEMAKER_DW.obj_o.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_o;
    Group44PACEMAKER_DW.obj_o.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    Group44PACEMAKER_DW.obj_o.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_Z_VENT_CTRL' */
    Group44PACEMAKER_DW.obj_d.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_d;
    Group44PACEMAKER_DW.obj_d.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    Group44PACEMAKER_DW.obj_d.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_VENT_GND_CTRL' */
    Group44PACEMAKER_DW.obj_l.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_l;
    Group44PACEMAKER_DW.obj_l.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    Group44PACEMAKER_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_VENT_PACE_CTRL' */
    Group44PACEMAKER_DW.obj_e.matlabCodegenIsDeleted = false;
    obj_0 = &Group44PACEMAKER_DW.obj_e;
    Group44PACEMAKER_DW.obj_e.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    Group44PACEMAKER_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_PACING_REF_PWM' */
    Group44PACEMAKER_DW.obj_m.matlabCodegenIsDeleted = false;
    obj_1 = &Group44PACEMAKER_DW.obj_m;
    Group44PACEMAKER_DW.obj_m.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(Group44PACEMAKER_DW.obj_m.MW_PWM_HANDLE);
    Group44PACEMAKER_DW.obj_m.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_VENT_CMP_REF_PWM' */
    Group44PACEMAKER_DW.obj_j.matlabCodegenIsDeleted = false;
    obj_1 = &Group44PACEMAKER_DW.obj_j;
    Group44PACEMAKER_DW.obj_j.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(3U, 2000.0, 0.0);
    MW_PWM_Start(Group44PACEMAKER_DW.obj_j.MW_PWM_HANDLE);
    Group44PACEMAKER_DW.obj_j.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/OUT_ATR_CMP_REF_PWM' */
    Group44PACEMAKER_DW.obj_c2.matlabCodegenIsDeleted = false;
    obj_1 = &Group44PACEMAKER_DW.obj_c2;
    Group44PACEMAKER_DW.obj_c2.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(6U, 2000.0, 0.0);
    MW_PWM_Start(Group44PACEMAKER_DW.obj_c2.MW_PWM_HANDLE);
    Group44PACEMAKER_DW.obj_c2.isSetupComplete = true;
  }
}

/* Model terminate function */
void Group44PACEMAKER_terminate(void)
{
  /* Terminate for MATLABSystem: '<S1>/in_ATR_CMP_DETECT' */
  if (!Group44PACEMAKER_DW.obj_c.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_c.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_c.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_c.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_c.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/in_ATR_CMP_DETECT' */

  /* Terminate for MATLABSystem: '<S1>/in_VENT_CMP_DETECT' */
  if (!Group44PACEMAKER_DW.obj.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/in_VENT_CMP_DETECT' */

  /* Terminate for MATLABSystem: '<S3>/OUT_ATR_GND_CTRL' */
  if (!Group44PACEMAKER_DW.obj_i.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_i.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_i.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_i.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_i.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_ATR_GND_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_ATR_PACE_CTRL' */
  if (!Group44PACEMAKER_DW.obj_d2.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_d2.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_d2.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_d2.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_d2.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_Z_ATR_CTRL' */
  if (!Group44PACEMAKER_DW.obj_n.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_n.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_n.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_n.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_PACE_CHARGE_CTRL' */
  if (!Group44PACEMAKER_DW.obj_b.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_b.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_PACE_GND_CTRL' */
  if (!Group44PACEMAKER_DW.obj_o.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_o.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_o.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_o.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_Z_VENT_CTRL' */
  if (!Group44PACEMAKER_DW.obj_d.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_d.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_d.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_d.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_d.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_Z_VENT_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_VENT_GND_CTRL' */
  if (!Group44PACEMAKER_DW.obj_l.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_l.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_VENT_GND_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_VENT_PACE_CTRL' */
  if (!Group44PACEMAKER_DW.obj_e.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_e.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(Group44PACEMAKER_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_VENT_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<S3>/OUT_PACING_REF_PWM' */
  if (!Group44PACEMAKER_DW.obj_m.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_m.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_m.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_m.isSetupComplete) {
      MW_PWM_Stop(Group44PACEMAKER_DW.obj_m.MW_PWM_HANDLE);
      MW_PWM_Close(Group44PACEMAKER_DW.obj_m.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_PACING_REF_PWM' */

  /* Terminate for MATLABSystem: '<S3>/OUT_VENT_CMP_REF_PWM' */
  if (!Group44PACEMAKER_DW.obj_j.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_j.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_j.isSetupComplete) {
      MW_PWM_Stop(Group44PACEMAKER_DW.obj_j.MW_PWM_HANDLE);
      MW_PWM_Close(Group44PACEMAKER_DW.obj_j.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_VENT_CMP_REF_PWM' */

  /* Terminate for MATLABSystem: '<S3>/OUT_ATR_CMP_REF_PWM' */
  if (!Group44PACEMAKER_DW.obj_c2.matlabCodegenIsDeleted) {
    Group44PACEMAKER_DW.obj_c2.matlabCodegenIsDeleted = true;
    if ((Group44PACEMAKER_DW.obj_c2.isInitialized == 1) &&
        Group44PACEMAKER_DW.obj_c2.isSetupComplete) {
      MW_PWM_Stop(Group44PACEMAKER_DW.obj_c2.MW_PWM_HANDLE);
      MW_PWM_Close(Group44PACEMAKER_DW.obj_c2.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/OUT_ATR_CMP_REF_PWM' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
