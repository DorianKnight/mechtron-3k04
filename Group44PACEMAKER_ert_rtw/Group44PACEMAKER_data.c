/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44PACEMAKER_data.c
 *
 * Code generated for Simulink model 'Group44PACEMAKER'.
 *
 * Model version                  : 1.98
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Sun Oct 16 18:38:54 2022
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
   * Referenced by: '<Root>/ATR_CMP_DETECT'
   */
  -1.0,

  /* Expression: SampleTime
   * Referenced by: '<Root>/VENT_CMP_DETECT'
   */
  -1.0,

  /* Expression: 320
   * Referenced by: '<Root>/p_ARP'
   */
  320.0,

  /* Expression: 320
   * Referenced by: '<Root>/p_VRP'
   */
  320.0,

  /* Expression: 5
   * Referenced by: '<Root>/p_aPaceWidth'
   */
  5.0,

  /* Expression: 200
   * Referenced by: '<Root>/p_hysteresisInterval'
   */
  200.0,

  /* Expression: 1000
   * Referenced by: '<Root>/p_lowrateInterval'
   */
  1000.0,

  /* Expression: 5
   * Referenced by: '<Root>/p_vPaceWidth'
   */
  5.0,

  /* Expression: 3
   * Referenced by: '<Root>/p_aPaceAmp'
   */
  3.0,

  /* Expression: 3
   * Referenced by: '<Root>/p_vPaceAmp'
   */
  3.0,

  /* Expression: 2.75
   * Referenced by: '<Root>/p_vSensitivity'
   */
  2.75,

  /* Expression: 2.75
   * Referenced by: '<Root>/p_aSensitivity'
   */
  2.75,

  /* Computed Parameter: mode_String
   * Referenced by: '<Root>/mode'
   */
  "VVI",

  /* Computed Parameter: p_hysteresis_Value
   * Referenced by: '<Root>/p_hysteresis'
   */
  false
};

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
