/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44PACEMAKER.h
 *
 * Code generated for Simulink model 'Group44PACEMAKER'.
 *
 * Model version                  : 1.140
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Wed Oct 19 19:11:16 2022
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
  real_T pulseDutyCycle;               /* '<S4>/Chart' */
  real_T cmpDutyCycle;                 /* '<S4>/Chart' */
  boolean_T ATR_GND_CTRL;              /* '<S4>/Chart' */
  boolean_T ATR_PACE_CTRL;             /* '<S4>/Chart' */
  boolean_T PACE_CHARGE_CTRL;          /* '<S4>/Chart' */
  boolean_T PACE_GND_CTRL;             /* '<S4>/Chart' */
  boolean_T VENT_GND_CTRL;             /* '<S4>/Chart' */
  boolean_T VENT_PACE_CTRL;            /* '<S4>/Chart' */
  boolean_T Z_ATR_CTRL;                /* '<S4>/Chart' */
  boolean_T Z_VENT_CTRL;               /* '<S4>/Chart' */
  boolean_T FRONTEND_CTRL;             /* '<S4>/Chart' */
} B_Group44PACEMAKER_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalRead_Group_T obj; /* '<S1>/input_VENT_CMP_DETECT' */
  freedomk64f_DigitalRead_Group_T obj_c;/* '<S1>/input_ATR_CMP_DETECT' */
  freedomk64f_PWMOutput_Group44_T obj_j;/* '<S3>/Output_VENT_CMP_REF_PWM' */
  freedomk64f_PWMOutput_Group44_T obj_m;/* '<S3>/Output_PACING_REF_PWM' */
  freedomk64f_PWMOutput_Group44_T obj_c2;/* '<S3>/Output_ATR_CMP_REF_PWM' */
  freedomk64f_DigitalWrite_Grou_T obj_d;/* '<S3>/Output_Z_VENT_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_n;/* '<S3>/Output_Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_e;/* '<S3>/Output_VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_l;/* '<S3>/Output_VENT_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_o;/* '<S3>/Output_PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_b;/* '<S3>/Output_PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_k;/* '<S3>/Output_FRONTEND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_d2;/* '<S3>/Output_ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_i;/* '<S3>/Output_ATR_GND_CTRL' */
  uint32_T temporalCounter_i1;         /* '<S4>/Chart' */
  uint8_T is_c6_Group44PACEMAKER;      /* '<S4>/Chart' */
  uint8_T is_active_c6_Group44PACEMAKER;/* '<S4>/Chart' */
} DW_Group44PACEMAKER_T;

/* Parameters (default storage) */
struct P_Group44PACEMAKER_T_ {
  real_T input_ATR_CMP_DETECT_SampleTime;/* Expression: SampleTime
                                          * Referenced by: '<S1>/input_ATR_CMP_DETECT'
                                          */
  real_T input_VENT_CMP_DETECT_SampleTim;/* Expression: SampleTime
                                          * Referenced by: '<S1>/input_VENT_CMP_DETECT'
                                          */
  real_T input_ARP_Value;              /* Expression: 320
                                        * Referenced by: '<S2>/input_ARP'
                                        */
  real_T input_VRP_Value;              /* Expression: 320
                                        * Referenced by: '<S2>/input_VRP'
                                        */
  real_T input_aPulseWidth_Value;      /* Expression: 5
                                        * Referenced by: '<S2>/input_aPulseWidth'
                                        */
  real_T input_LRL_Value;              /* Expression: 666
                                        * Referenced by: '<S2>/input_LRL'
                                        */
  real_T input_vPulseWidth_Value;      /* Expression: 5
                                        * Referenced by: '<S2>/input_vPulseWidth'
                                        */
  real_T input_aPulseAmp_Value;        /* Expression: 3
                                        * Referenced by: '<S2>/input_aPulseAmp'
                                        */
  real_T input_vPulseAmp_Value;        /* Expression: 3
                                        * Referenced by: '<S2>/input_vPulseAmp'
                                        */
  real_T input_vSensitivity_Value;     /* Expression: 3.8
                                        * Referenced by: '<S2>/input_vSensitivity'
                                        */
  real_T input_aSensitivity_Value;     /* Expression: 3.8
                                        * Referenced by: '<S2>/input_aSensitivity'
                                        */
  char_T mode_String[256];             /* Computed Parameter: mode_String
                                        * Referenced by: '<S2>/mode'
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
 * '<S1>'   : 'Group44PACEMAKER/InputPins'
 * '<S2>'   : 'Group44PACEMAKER/Inputs'
 * '<S3>'   : 'Group44PACEMAKER/OutputPins'
 * '<S4>'   : 'Group44PACEMAKER/Stateflow'
 * '<S5>'   : 'Group44PACEMAKER/OutputPins/Requirements table'
 * '<S6>'   : 'Group44PACEMAKER/OutputPins/Requirements table/Requirements Table'
 * '<S7>'   : 'Group44PACEMAKER/Stateflow/Chart'
 */
#endif                                 /* RTW_HEADER_Group44PACEMAKER_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
