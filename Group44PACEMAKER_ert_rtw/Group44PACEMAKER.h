/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44PACEMAKER.h
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

#ifndef RTW_HEADER_Group44PACEMAKER_h_
#define RTW_HEADER_Group44PACEMAKER_h_
#ifndef Group44PACEMAKER_COMMON_INCLUDES_
#define Group44PACEMAKER_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* Group44PACEMAKER_COMMON_INCLUDES_ */

#include "Group44PACEMAKER_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  char_T mode[256];
  real_T dutyCycle;                    /* '<Root>/Chart' */
  real_T cmpDutyCycle;                 /* '<Root>/Chart' */
  boolean_T ATR_GND_CTRL;              /* '<Root>/Chart' */
  boolean_T ATR_PACE_CTRL;             /* '<Root>/Chart' */
  boolean_T PACE_CHARGE_CTRL;          /* '<Root>/Chart' */
  boolean_T PACE_GND_CTRL;             /* '<Root>/Chart' */
  boolean_T VENT_GND_CTRL;             /* '<Root>/Chart' */
  boolean_T VENT_PACE_CTRL;            /* '<Root>/Chart' */
  boolean_T Z_ATR_CTRL;                /* '<Root>/Chart' */
  boolean_T Z_VENT_CTRL;               /* '<Root>/Chart' */
} B_Group44PACEMAKER_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalRead_Group_T obj; /* '<Root>/VENT_CMP_DETECT' */
  freedomk64f_DigitalRead_Group_T obj_a;/* '<Root>/ATR_CMP_DETECT' */
  freedomk64f_PWMOutput_Group44_T obj_j;/* '<Root>/VENT_CMP_REF_PWM' */
  freedomk64f_PWMOutput_Group44_T obj_m;/* '<Root>/PACING_REF_PWM' */
  freedomk64f_PWMOutput_Group44_T obj_c;/* '<Root>/ATR_CMP_REF_PWM' */
  freedomk64f_DigitalWrite_Grou_T obj_d;/* '<Root>/Z_VENT_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_n;/* '<Root>/Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_e;/* '<Root>/VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_l;/* '<Root>/VENT_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_o;/* '<Root>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_b;/* '<Root>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_cq;/* '<Root>/Digital Write1' */
  freedomk64f_DigitalWrite_Grou_T obj_h;/* '<Root>/Digital Write' */
  freedomk64f_DigitalWrite_Grou_T obj_d2;/* '<Root>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_i;/* '<Root>/ATR_GND_CTRL' */
  uint32_T temporalCounter_i1;         /* '<Root>/Chart' */
  uint8_T is_c6_Group44PACEMAKER;      /* '<Root>/Chart' */
  uint8_T is_active_c6_Group44PACEMAKER;/* '<Root>/Chart' */
} DW_Group44PACEMAKER_T;

/* Parameters (default storage) */
struct P_Group44PACEMAKER_T_ {
  real_T ATR_CMP_DETECT_SampleTime;    /* Expression: SampleTime
                                        * Referenced by: '<Root>/ATR_CMP_DETECT'
                                        */
  real_T VENT_CMP_DETECT_SampleTime;   /* Expression: SampleTime
                                        * Referenced by: '<Root>/VENT_CMP_DETECT'
                                        */
  real_T p_ARP_Value;                  /* Expression: 320
                                        * Referenced by: '<Root>/p_ARP'
                                        */
  real_T p_VRP_Value;                  /* Expression: 320
                                        * Referenced by: '<Root>/p_VRP'
                                        */
  real_T p_aPaceWidth_Value;           /* Expression: 5
                                        * Referenced by: '<Root>/p_aPaceWidth'
                                        */
  real_T p_hysteresisInterval_Value;   /* Expression: 200
                                        * Referenced by: '<Root>/p_hysteresisInterval'
                                        */
  real_T p_lowrateInterval_Value;      /* Expression: 1000
                                        * Referenced by: '<Root>/p_lowrateInterval'
                                        */
  real_T p_vPaceWidth_Value;           /* Expression: 5
                                        * Referenced by: '<Root>/p_vPaceWidth'
                                        */
  real_T p_aPaceAmp_Value;             /* Expression: 3
                                        * Referenced by: '<Root>/p_aPaceAmp'
                                        */
  real_T p_vPaceAmp_Value;             /* Expression: 3
                                        * Referenced by: '<Root>/p_vPaceAmp'
                                        */
  real_T p_vSensitivity_Value;         /* Expression: 2.75
                                        * Referenced by: '<Root>/p_vSensitivity'
                                        */
  real_T p_aSensitivity_Value;         /* Expression: 2.75
                                        * Referenced by: '<Root>/p_aSensitivity'
                                        */
  char_T mode_String[256];             /* Computed Parameter: mode_String
                                        * Referenced by: '<Root>/mode'
                                        */
  boolean_T p_hysteresis_Value;        /* Computed Parameter: p_hysteresis_Value
                                        * Referenced by: '<Root>/p_hysteresis'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_Group44PACEMAKER_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_Group44PACEMAKER_T Group44PACEMAKER_P;

/* Block signals (default storage) */
extern B_Group44PACEMAKER_T Group44PACEMAKER_B;

/* Block states (default storage) */
extern DW_Group44PACEMAKER_T Group44PACEMAKER_DW;

/* Model entry point functions */
extern void Group44PACEMAKER_initialize(void);
extern void Group44PACEMAKER_step(void);
extern void Group44PACEMAKER_terminate(void);

/* Real-time Model object */
extern RT_MODEL_Group44PACEMAKER_T *const Group44PACEMAKER_M;
extern volatile boolean_T stopRequested;
extern volatile boolean_T runModel;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<Root>/Scope' : Unused code path elimination
 * Block '<Root>/Scope1' : Unused code path elimination
 * Block '<Root>/Scope2' : Unused code path elimination
 * Block '<Root>/Scope3' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'Group44PACEMAKER'
 * '<S1>'   : 'Group44PACEMAKER/Chart'
 */
#endif                                 /* RTW_HEADER_Group44PACEMAKER_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
