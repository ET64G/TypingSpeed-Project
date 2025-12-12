# Typing Speed Test Application - Flowchart

## Main Application Flow

```mermaid
flowchart TD
    Start([Application Start]) --> Init[Initialize Application]
    Init --> CreateUI[Create UI Components]
    CreateUI --> LoadText[Load Sample Text]
    LoadText --> Wait[Wait for User Action]
    
    Wait -->|User clicks Start| CheckText{Text Available?}
    CheckText -->|No| Error1[Show Error Message]
    Error1 --> Wait
    CheckText -->|Yes| CheckRunning{Test Running?}
    CheckRunning -->|Yes| Wait
    CheckRunning -->|No| StartTest[Start Test]
    
    StartTest --> EnableInput[Enable Input Field]
    EnableInput --> BindEvents[Bind Keyboard Events]
    BindEvents --> StartTimer[Start Timer Loop]
    StartTimer --> TypingLoop[User Types]
    
    TypingLoop --> KeyPress[On Key Press]
    KeyPress --> CheckSpecial{Special Key?}
    CheckSpecial -->|Navigation| Allow[Allow Key]
    CheckSpecial -->|Clipboard| Block[Block Key]
    CheckSpecial -->|Normal| Allow
    Allow --> KeyRelease[On Key Release]
    Block --> TypingLoop
    
    KeyRelease --> UpdateInput[Update User Input]
    UpdateInput --> Compare[Compare with Sample Text]
    Compare --> CalcMetrics[Calculate Metrics]
    CalcMetrics --> CheckMode{Test Mode?}
    
    CheckMode -->|Fixed Text| CheckComplete{Text Complete?}
    CheckMode -->|Fixed Time| TimerCheck[Check Timer]
    
    CheckComplete -->|Yes| EndTest[End Test]
    CheckComplete -->|No| TimerCheck
    
    TimerCheck --> TimeReached{Time Limit Reached?}
    TimeReached -->|Yes| EndTest
    TimeReached -->|No| ScheduleTimer[Schedule Next Timer Update]
    ScheduleTimer --> TypingLoop
    
    EndTest --> StopController[Stop Test Controller]
    StopController --> DisableInput[Disable Input Field]
    DisableInput --> ShowResults[Show Results Window]
    ShowResults --> Wait
    
    Wait -->|User clicks Reset| ResetTest[Reset Test]
    ResetTest --> ClearInput[Clear Input Field]
    ClearInput --> DisableInput2[Disable Input Field]
    DisableInput2 --> ResetController[Reset Controller]
    ResetController --> Wait
    
    Wait -->|User changes Mode| ModeChange[On Mode Change]
    ModeChange --> CheckRunning2{Test Running?}
    CheckRunning2 -->|Yes| Warning[Show Warning]
    CheckRunning2 -->|No| LoadText
    Warning --> Wait
    
    Wait -->|User changes Difficulty| DiffChange[On Difficulty Change]
    DiffChange --> LoadText
    
    Wait -->|User clicks New Text| LoadText
    
    Wait -->|User closes Window| End([Application End])
```

## Test Controller Flow

```mermaid
flowchart TD
    Start([Test Controller Start]) --> Init[Initialize State Variables]
    Init --> Idle[State: Idle]
    
    Idle -->|start_test called| StartTest[Start Test]
    StartTest --> SetRunning[Set State: Running]
    SetRunning --> RecordStart[Record Start Time]
    RecordStart --> ResetMetrics[Reset All Metrics]
    ResetMetrics --> Running[State: Running]
    
    Running -->|update_input called| GetInput[Get User Input]
    GetInput --> CompareChars[Compare Characters]
    CompareChars --> CountCorrect[Count Correct/Incorrect]
    CountCorrect --> CheckMode{Test Mode?}
    
    CheckMode -->|Fixed Text| CheckLength{Input Length >= Sample Length?}
    CheckMode -->|Fixed Time| UpdateTime[Update Time]
    
    CheckLength -->|Yes| StopTest[Stop Test]
    CheckLength -->|No| UpdateTime
    
    Running -->|update_time called| UpdateTime
    UpdateTime --> CalcElapsed[Calculate Elapsed Time]
    CalcElapsed --> CheckTimeLimit{Time >= Limit?}
    
    CheckTimeLimit -->|Yes| StopTest
    CheckTimeLimit -->|No| Running
    
    StopTest --> SetCompleted[Set State: Completed]
    SetCompleted --> CalcFinal[Calculate Final Results]
    CalcFinal --> CalcWPM[Calculate WPM]
    CalcWPM --> CalcAccuracy[Calculate Accuracy]
    CalcAccuracy --> CountWords[Count Words Completed]
    CountWords --> Completed[State: Completed]
    
    Completed -->|get_results called| ReturnResults[Return Results Dictionary]
    ReturnResults --> Completed
    
    Running -->|reset_test called| Reset[Reset Test]
    Completed -->|reset_test called| Reset
    Reset --> ClearAll[Clear All Variables]
    ClearAll --> Idle
```

## Input Processing Flow

```mermaid
flowchart TD
    Start([User Types Key]) --> KeyPress[Key Press Event]
    KeyPress --> CheckRunning{Test Running?}
    CheckRunning -->|No| Block1[Block Input]
    Block1 --> End1([End])
    
    CheckRunning -->|Yes| CheckKeyType{Key Type?}
    CheckKeyType -->|Navigation| Allow1[Allow Key]
    CheckKeyType -->|Control+C/V/X/A| Block2[Block Key]
    CheckKeyType -->|Normal| Allow1
    
    Allow1 --> KeyRelease[Key Release Event]
    Block2 --> End1
    
    KeyRelease --> CheckRunning2{Test Running?}
    CheckRunning2 -->|No| End2([End])
    CheckRunning2 -->|Yes| GetInput[Get Current Input Text]
    GetInput --> UpdateUserInput[Update user_input Variable]
    UpdateUserInput --> CallController[Call controller.update_input]
    CallController --> Compare[Compare Input with Sample]
    Compare --> Calculate[Calculate Metrics]
    Calculate --> CheckComplete{Test Complete?}
    
    CheckComplete -->|Yes| EndTest[End Test]
    CheckComplete -->|No| Continue[Continue Test]
    EndTest --> End2
    Continue --> End2
```

## Results Display Flow

```mermaid
flowchart TD
    Start([Test Completed]) --> GetResults[Get Results from Controller]
    GetResults --> CreateWindow[Create Results Window]
    CreateWindow --> CenterWindow[Center Window on Parent]
    CenterWindow --> MakeModal[Make Window Modal]
    MakeModal --> CreateUI[Create UI Components]
    
    CreateUI --> ShowTitle[Display Title: Test Results]
    ShowTitle --> ShowWPM[Display WPM - Large and Bold]
    ShowWPM --> ShowAccuracy[Display Accuracy Percentage]
    ShowAccuracy --> ShowTime[Display Time Taken]
    ShowTime --> ShowSeparator[Show Separator Line]
    ShowSeparator --> ShowDetailsLabel[Display Details Label]
    ShowDetailsLabel --> ShowTotalChars[Display Total Characters]
    ShowTotalChars --> ShowCorrect[Display Correct Characters - Green]
    ShowCorrect --> ShowIncorrect[Display Incorrect Characters - Red]
    ShowIncorrect --> ShowWords[Display Words Completed]
    ShowWords --> ShowMode[Display Test Mode]
    ShowMode --> ShowCloseButton[Display Close Button]
    ShowCloseButton --> WaitClose[Wait for User to Close]
    
    WaitClose -->|User clicks Close| DestroyWindow[Destroy Window]
    DestroyWindow --> End([End])
```

## Text Generation Flow

```mermaid
flowchart TD
    Start([Load Sample Text Requested]) --> CheckRunning{Test Running?}
    CheckRunning -->|Yes| ShowWarning[Show Warning Message]
    ShowWarning --> End1([End])
    
    CheckRunning -->|No| GetDifficulty[Get Selected Difficulty]
    GetDifficulty --> CheckDiff{Difficulty Level?}
    
    CheckDiff -->|Easy| SelectEasy[Select EASY_TEXTS]
    CheckDiff -->|Medium| SelectMedium[Select MEDIUM_TEXTS]
    CheckDiff -->|Hard| SelectHard[Select HARD_TEXTS]
    
    SelectEasy --> RandomSelect[Randomly Select Text]
    SelectMedium --> RandomSelect
    SelectHard --> RandomSelect
    
    RandomSelect --> SetSampleText[Set sample_text Variable]
    SetSampleText --> UpdateDisplay[Update Text Display]
    UpdateDisplay --> EnableDisplay[Enable Display for Update]
    EnableDisplay --> ClearDisplay[Clear Display]
    ClearDisplay --> InsertText[Insert New Text]
    InsertText --> DisableDisplay[Disable Display]
    DisableDisplay --> End2([End])
```

## ASCII Art Flowchart (Alternative Format)

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION START                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Initialize App  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Create UI      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Load Sample    │
              │      Text       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Wait for User   │
              │     Action      │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   [Start]        [Reset]      [Change Mode]
        │              │              │
        ▼              ▼              ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ Start   │   │ Reset   │   │ Reload  │
   │  Test   │   │  Test   │   │  Text   │
   └────┬────┘   └────┬────┘   └────┬────┘
        │             │              │
        │             └──────┬───────┘
        │                    │
        ▼                    ▼
   ┌─────────┐         ┌─────────┐
   │ Enable  │         │  Wait   │
   │  Input  │         │  Loop   │
   └────┬────┘         └─────────┘
        │
        ▼
   ┌─────────┐
   │  User   │
   │  Types  │
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ Compare │
   │  Input  │
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ Check   │
   │  Mode   │
   └────┬────┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
┌─────┐  ┌─────┐
│Time │  │Text │
│Limit│  │Done │
└──┬──┘  └──┬──┘
   │        │
   └───┬────┘
       │
       ▼
   ┌─────────┐
   │  End    │
   │  Test   │
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │  Show   │
   │ Results │
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │  Wait   │
   │  Loop   │
   └─────────┘
```

