/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44PACEMAKER_data.c
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

/* Block parameters (default storage) */
P_Group44PACEMAKER_T Group44PACEMAKER_P = {
  /* Expression: SampleTime
   * Referenced by: '<S1>/in_ATR_CMP_DETECT'
   */
  -1.0,

  /* Expression: SampleTime
   * Referenced by: '<S1>/in_VENT_CMP_DETECT'
   */
  -1.0,

  /* Expression: 320
   * Referenced by: '<S2>/in_p_ARP'
   */
  320.0,

  /* Expression: 320
   * Referenced by: '<S2>/in_p_VRP'
   */
  320.0,

  /* Expression: 5
   * Referenced by: '<S2>/in_p_aPaceWidth'
   */
  5.0,

  /* Expression: 200
   * Referenced by: '<S2>/in_p_hysteresisInterval'
   */
  200.0,

  /* Expression: 1000
   * Referenced by: '<S2>/in_p_lowrateInterval'
   */
  1000.0,

  /* Expression: 5
   * Referenced by: '<S2>/in_p_vPaceWidth'
   */
  5.0,

  /* Expression: 3
   * Referenced by: '<S2>/in_p_aPaceAmp'
   */
  3.0,

  /* Expression: 3
   * Referenced by: '<S2>/in_p_vPaceAmp'
   */
  3.0,

  /* Expression: 2.75
   * Referenced by: '<S2>/in_p_vSensitivity'
   */
  2.75,

  /* Expression: 2.75
   * Referenced by: '<S2>/in_p_aSensitivity'
   */
  2.75,

  /* Computed Parameter: mode_String
   * Referenced by: '<S2>/mode'
   */
  "VOO",

  /* Computed Parameter: in_p_hysteresis_Value
   * Referenced by: '<S2>/in_p_hysteresis'
   */
  false
};

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
