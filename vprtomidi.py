#pitch bending is NOT supported

from midiutil import MIDIFile

import zipfile
import json
import sys

path = input("[INPP] path: ")

ZIP = zipfile.ZipFile(path, "r")

print("[INFO] files found:")
print("[INFO] {}".format(ZIP.namelist()))

print("[INFO] files info:")
for i in ZIP.infolist():
    print("[INFO] {} real size: {} zip size: {}".format(i.filename, i.file_size, i.compress_size))

print("[INFO] openning Project/sequence.json ...")
vpr = json.loads(ZIP.open("Project/sequence.json").read())

TEMPO = vpr["masterTrack"]["tempo"]["events"]
print("[INFO] tempo: ")
for i in TEMPO:
    print("[INFO] {}".format(i))

TRACKTYPES = [int(i["type"]) for i in vpr["tracks"]]
print("[INFO] tracktypes: {}".format(TRACKTYPES))

TRACKS = len(TRACKTYPES) - sum(TRACKTYPES)
print("[INFO] convertable tracks: {}".format(TRACKS))

mf = MIDIFile(TRACKS, removeDuplicates = False)

offset = 0
tracknum = 0

for track in vpr["tracks"]:
    if(track["type"] == 1):
        offset += 1
        continue
    time = 0
    mf.addTrackName(tracknum, time, track["name"])
    for tempo in TEMPO:
        mf.addTempo(tracknum, tempo["pos"] / 480, tempo["value"] / 100)
    try:
        for part in track["parts"]:
            try:
                for note in part["notes"]:
                    mf.addNote(tracknum, 0, note["number"], (note["pos"] + part["pos"]) / 480, note["duration"] / 480, note["velocity"])
            except KeyError:
                print("[WARN] part {}, in track {}, does not have \"notes\" key".format(part["name"], track["name"]))
    except KeyError:
        print("[WARN] track {} does not have \"parts\" key".format(track["name"]))
    tracknum += 1

with open(path+".mid", 'wb') as outf:
    mf.writeFile(outf)

ZIP.close()

print("[INFO] finished export")


"""
to implement:
MusicalEditorViewModel
VSMAbsTick
Point
IntPtr
"""

"""
class ArgumentException(ValueError):
    pass

class ArgumentNullException(ArgumentException):
    pass

class ArgumentTypeException(TypeError):
    pass

def IntPtr(obj):
    return obj._cppObjPtr

class WIVSMPart(IntPtr):
    #IntPtr _cppObjPtr = IntPtr.Zero

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern VSMResult VIS_VSM_WIVSMPart_lastError(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern IntPtr VIS_VSM_WIVSMPart_sequence(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern IntPtr VIS_VSM_WIVSMPart_parent(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern VSMPartType VIS_VSM_WIVSMPart_type(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern IntPtr VIS_VSM_WIVSMPart_name(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #[return: MarshalAs(UnmanagedType.U1)]
    #private static extern bool VIS_VSM_WIVSMPart_setName(IntPtr cppobjptr, [MarshalAs(UnmanagedType.LPWStr), In] string name);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #[return: MarshalAs(UnmanagedType.U1)]
    #private static extern bool VIS_VSM_WIVSMPart_isSelected(IntPtr cppobjptr);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern void VIS_VSM_WIVSMPart_select(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool select);

    #[DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    #private static extern int VIS_VSM_WIVSMPart_posTick(IntPtr cppobjptr);

    def Equals(self, obj):
        if (obj == null):
            return false
        try:
            wivsmPart = type(self)(obj)
        except (TypeError, ValueError) as e:
            return false
        return self._cppObjPtr == wivsmPart._cppObjPtr

    def GetHashCode(self):
        return int(self._cppObjPtr)

    def __init__(self, part):
        if (isinstance(part, IntPtr)):
            if (pPart == IntPtr.Zero):
                raise ArgumentException("アンマネージオブジェクトではない")
            self._cppObjPtr = pPart
        elif (isinstance(part, WIVSMPart)):
            if (part == null):
                raise ArgumentNullException("オブジェクトがnull")
            self._cppObjPtr = part._cppObjPtr
        else:
            raise ArgumentTypeException("Wrong type given to the constructor")

    public VSMResult LastError
    {
      get
      {
        return WIVSMPart.VIS_VSM_WIVSMPart_lastError(this._cppObjPtr);
      }
    }

    public WIVSMSequence Sequence
    {
      get
      {
        IntPtr pSequence = WIVSMPart.VIS_VSM_WIVSMPart_sequence(this._cppObjPtr);
        if (!(pSequence == IntPtr.Zero))
          return new WIVSMSequence(pSequence, false);
        return (WIVSMSequence) null;
      }
    }

    public WIVSMTrack Parent
    {
      get
      {
        IntPtr pTrack = WIVSMPart.VIS_VSM_WIVSMPart_parent(this._cppObjPtr);
        if (!(pTrack == IntPtr.Zero))
          return new WIVSMTrack(pTrack);
        return (WIVSMTrack) null;
      }
    }

    public VSMPartType Type
    {
      get
      {
        return WIVSMPart.VIS_VSM_WIVSMPart_type(this._cppObjPtr);
      }
    }

    public string Name
    {
      get
      {
        return Marshal.PtrToStringUni(WIVSMPart.VIS_VSM_WIVSMPart_name(this._cppObjPtr));
      }
    }

    public bool IsSelected
    {
      get
      {
        return WIVSMPart.VIS_VSM_WIVSMPart_isSelected(this._cppObjPtr);
      }
      set
      {
        WIVSMPart.VIS_VSM_WIVSMPart_select(this._cppObjPtr, value);
      }
    }

    public VSMAbsTick AbsPosition
    {
      get
      {
        return new VSMAbsTick(WIVSMPart.VIS_VSM_WIVSMPart_posTick(this._cppObjPtr));
      }
    }

    public bool SetName(string name)
    {
      return WIVSMPart.VIS_VSM_WIVSMPart_setName(this._cppObjPtr, name);
    }

    public VSMAbsTick AbsBegin
    {
      get
      {
        if (this.Type == VSMPartType.Midi)
          return new WIVSMMidiPart(this).AbsPosition;
        WIVSMAudioPart wivsmAudioPart = new WIVSMAudioPart(this);
        return new VSMAbsTick(wivsmAudioPart.AbsPosition.Tick + wivsmAudioPart.Region.TickBegin);
      }
    }

    public virtual VSMAbsTick AbsEnd
    {
      get
      {
        if (this.Type != VSMPartType.Midi)
          return new WIVSMAudioPart(this).AbsEnd;
        return new WIVSMMidiPart(this).AbsEnd;
      }
    }

    public int DurationTick
    {
      get
      {
        int num;
        if (this.Type == VSMPartType.Midi)
        {
          num = new WIVSMMidiPart(this).Duration.Tick;
        }
        else
        {
          WIVSMAudioPart wivsmAudioPart = new WIVSMAudioPart(this);
          num = wivsmAudioPart.Region.TickEnd - wivsmAudioPart.Region.TickBegin;
        }
        return num;
      }
    }

    public WIVSMEffectManager EffectManager
    {
      get
      {
        if (this.Type == VSMPartType.Midi)
          return new WIVSMMidiPart(this)?.EffectManager;
        if (this.Type != VSMPartType.Audio)
          return (WIVSMEffectManager) null;
        return new WIVSMAudioPart(this)?.EffectManager;
      }
    }

    public double GetBeginTime(double presendTime)
    {
      return this.Parent.Parent.GetMillisecFromTick(new VSMAbsTick(0), this.AbsPosition) / 1000.0 - presendTime;
    }

    public double GetDurationTime(double presendTime)
    {
      return this.Parent.Parent.GetMillisecFromTick(this.AbsPosition, this.AbsEnd) / 1000.0 - presendTime;
    }

    public string PartFilePath
    {
      get
      {
        string str = (string) null;
        if (this.Type == VSMPartType.Midi)
        {
          WIVSMMidiPart wivsmMidiPart = this as WIVSMMidiPart;
          if (wivsmMidiPart != null)
            str = wivsmMidiPart.GetRenderedFilePath();
        }
        else if (this.Type == VSMPartType.Audio)
        {
          WIVSMAudioPart wivsmAudioPart = this as WIVSMAudioPart;
          if (wivsmAudioPart != null)
            str = wivsmAudioPart.GetWaveFilePath();
        }
        return str;
      }
    }

    public string Description
    {
      get
      {
        return "" + string.Format("_cppObjPtr: {0:x}\n", (object) this._cppObjPtr.ToInt64()) + string.Format("Sequence: {0:x}\n", (object) this.Sequence.GetHashCode()) + string.Format("Type: {0}\n", (object) this.Type) + string.Format("Name: {0}\n", (object) this.Name) + string.Format("AbsPosition.Tick: {0}\n", (object) this.AbsPosition.Tick) + string.Format("DurationTick: {0}\n", (object) this.DurationTick) + string.Format("PartFilePath: {0}\n", (object) this.PartFilePath);
      }
    }
    
"""

"""
def pitchcurve(vm, part):
    #VSMAbsTick _abs1;
    #VSMAbsTick _abs2;
    #Point _pt
    #FastCanvas xCanvasPitchCurve
    if (vm == null):
        return null
    if (vm.Sequence == null or part == null):
        return null
    sequence = vm.Sequence
    numrenderedscore = part.numrenderedscore
    if (numrenderedscore == 0):
        return null
    #UIPitchCurve uiPitchCurve1 = new UIPitchCurve()
    #{
    #    VM = vm,
    #    Part = midiPart,
    #    PitchCurvePen = this._penPitchCurve
    #}
    _abs1.Tick = 0
    _abs2.Tick = part.AbsPosition.Tick
    baseMsec = sequence.GetMillisecFromTick(_abs1, _abs2) - sequence.PresendTime
    endMsec = sequence.GetMillisecFromTick(_abs1, part.AbsEnd)
    num1 = 0
    sampleFromMillisec = sequence.GetSampleFromMillisec(endMsec - baseMsec, sequence.GetSamplingRate())
    if(sampleFromMillisec <= 0 or sequence.NumSampleInFrame <= 0):
        num2 = 0
    else:
        num2 = sampleFromMillisec / sequence.NumSampleInFrame
    minValue = #float.MinValue
    num3 = 1
    num4 = 2
    num5 = minValue
    index = num1
    #Point point1
    while (index <= num2 and numRenderedScore > index):
        renderedScore = part.GetRenderedScore(index)
        if (renderedScore != null):
            num6 = 0
            if (num4 == 0):
                num6 = renderedScore.ExpPit
            elif (num4 == 1):
                num6 = renderedScore.PbPit
            elif (num4 == 2):
                num6 = renderedScore.VibPit
        if (num6 != minValue):
            num7 = int((num6 + 6900) / 100 - MainViewModel.MinkeyNumber)
            num8 = float((MainViewModel.MaxKeyCount - 1 - num7) * vm.OneKeyHeight + vm.OneKeyHeight / 2.0) - ((num6 + 6900.0 - (num7 * 100)) * (vm.OneKeyHeight / 100.0))
            msecEnd = baseMsec + sequence.GetMillisecFromSample(index * sequence.NumSampleInFrame, sequence.GetSamplingRate())
            _abs1.Tick = 0
            _pt.X = sequence.GetTickFromMillisec(_abs1, msecEnd) * vm.WidthPerTick
            _pt.Y = num8
            if (num5 == minValue and uiPitchCurve1.Points.Count != 0):
                uiPitchCurve2 = uiPitchCurve1
                point1 = uiPitchCurve1.Points[0]
                x1 = point1.X
                ##Canvas.SetLeft((UIElement) uiPitchCurve2, x1)
                ##Canvas.SetTop((UIElement) uiPitchCurve1, 0.0)
                uiPitchCurve3 = uiPitchCurve1
                point1 = uiPitchCurve1.Points[0]
                x2 = point1.X
                point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1]
                x3 = point1.X
                point1 = uiPitchCurve1.Points[0]
                x4 = point1.X
                num9 = x3 - x4
                length = x2 + num9
                ##Canvas.SetRight((UIElement) uiPitchCurve3, length)
                ##Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0)
                ##xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1)
                #uiPitchCurve1 = new UIPitchCurve()
                #{
                #    VM = vm,
                #    Part = midiPart,
                #    PitchCurvePen = this._penPitchCurve
                #}
            uiPitchCurve1.Points.Add(_pt)
        num5 = num6
            if (1000 <= uiPitchCurve1.Points.Count):
                point2 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1]
                uiPitchCurve2 = uiPitchCurve1
                point1 = uiPitchCurve1.Points[0]
                x1 = point1.X
                ##Canvas.SetLeft((UIElement) uiPitchCurve2, x1)
                ##Canvas.SetTop((UIElement) uiPitchCurve1, 0.0)
                uiPitchCurve3 = uiPitchCurve1
                point1 = uiPitchCurve1.Points[0]
                x2 = point1.X
                point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1]
                x3 = point1.X
                point1 = uiPitchCurve1.Points[0]
                x4 = point1.X
                num7 = x3 - x4
                length = x2 + num7
                ##Canvas.SetRight((UIElement) uiPitchCurve3, length)
                ##Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0)
                ##xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1)
                #uiPitchCurve1 = new UIPitchCurve()
                #{
                #    VM = vm,
                #    Part = midiPart,
                #    PitchCurvePen = this._penPitchCurve
                #}
                uiPitchCurve1.Points.Add(point2)
        index += num3
    if (uiPitchCurve1.Points.Count == 0):
        return null
    uiPitchCurve4 = uiPitchCurve1
    point1 = uiPitchCurve1.Points[0]
    x5 = point1.X
    ##Canvas.SetLeft((UIElement) uiPitchCurve4, x5)
    ##Canvas.SetTop((UIElement) uiPitchCurve1, 0.0)
    uiPitchCurve5 = uiPitchCurve1
    point1 = uiPitchCurve1.Points[0]
    x6 = point1.X
    point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1]
    x7 = point1.X
    point1 = uiPitchCurve1.Points[0]
    x8 = point1.X
    num10 = x7 - x8
    length1 = x6 + num10
    ##Canvas.SetRight((UIElement) uiPitchCurve5, length1)
    ##Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0)
    ##xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1)
"""
