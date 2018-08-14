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
def pitchcurve(vm, part):
    if(vm == null) return null
    if(vm.Sequence == null or part == null) return null
    sequence = vm.Sequence
    numrenderedscore = part.numrenderedscore
    if(numrenderedscore == 0) return null
    #VSMAbsTick _abs1;
    #VSMAbsTick _abs2;
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
    point1x = 0
    point1y = 0
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
            num7 = (int) ((num6 + 6900)/100 - MainViewModel.MinkeyNumber)
"""

"""
VOCALOID pitch curve calculation:
seems to require engine’s wave render

private void InsertPitchCurve(MusicalEditorViewModel vm, WIVSMMidiPart midiPart)
    {
      if (vm?.Sequence == null || midiPart == null)
        return;
      WIVSMSequence sequence = vm.Sequence;
      ulong numRenderedScore = midiPart.NumRenderedScore;
      if (numRenderedScore == 0UL)
        return;
      UIPitchCurve uiPitchCurve1 = new UIPitchCurve()
      {
        VM = vm,
        Part = midiPart,
        PitchCurvePen = this._penPitchCurve
      };
      this._abs1.Tick = 0;
      this._abs2.Tick = midiPart.AbsPosition.Tick;
      double baseMsec = sequence.GetMillisecFromTick(this._abs1, this._abs2) - (double) sequence.PresendTime;
      double endMsec = sequence.GetMillisecFromTick(this._abs1, midiPart.AbsEnd);
      long num1 = 0;
      ulong num2 = ((Func<ulong>) (() =>
      {
        long sampleFromMillisec = sequence.GetSampleFromMillisec(endMsec - baseMsec, sequence.GetSamplingRate());
        if (sampleFromMillisec <= 0L || sequence.NumSampleInFrame <= 0L)
          return 0;
        return (ulong) (sampleFromMillisec / sequence.NumSampleInFrame);
      }))();
      float minValue = float.MinValue;
      ulong num3 = 1;
      int num4 = 2;
      float num5 = minValue;
      ulong index = (ulong) num1;
      Point point1;
      while (index <= num2 && numRenderedScore > index)
      {
        VSMRenderedScoreData renderedScore = midiPart.GetRenderedScore(index);
        if (renderedScore != null)
        {
          float num6 = 0.0f;
          switch (num4)
          {
            case 0:
              num6 = renderedScore.ExpPit;
              break;
            case 1:
              num6 = renderedScore.PbPit;
              break;
            case 2:
              num6 = renderedScore.VibPit;
              break;
          }
          if ((double) num6 != (double) minValue)
          {
            int num7 = (int) (((double) num6 + 6900.0) / 100.0) - MainViewModel.MinKeyNumber;
            float num8 = (float) ((double) (MainViewModel.MaxKeyCount - 1 - num7) * vm.OneKeyHeight + vm.OneKeyHeight / 2.0) - (float) (((double) num6 + 6900.0 - (double) (num7 * 100)) * (vm.OneKeyHeight / 100.0));
            double msecEnd = baseMsec + sequence.GetMillisecFromSample((long) index * sequence.NumSampleInFrame, sequence.GetSamplingRate());
            this._abs1.Tick = 0;
            this._pt.X = (double) sequence.GetTickFromMillisec(this._abs1, msecEnd) * vm.WidthPerTick;
            this._pt.Y = (double) num8;
            if ((double) num5 == (double) minValue && uiPitchCurve1.Points.Count != 0)
            {
              UIPitchCurve uiPitchCurve2 = uiPitchCurve1;
              point1 = uiPitchCurve1.Points[0];
              double x1 = point1.X;
              Canvas.SetLeft((UIElement) uiPitchCurve2, x1);
              Canvas.SetTop((UIElement) uiPitchCurve1, 0.0);
              UIPitchCurve uiPitchCurve3 = uiPitchCurve1;
              point1 = uiPitchCurve1.Points[0];
              double x2 = point1.X;
              point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1];
              double x3 = point1.X;
              point1 = uiPitchCurve1.Points[0];
              double x4 = point1.X;
              double num9 = x3 - x4;
              double length = x2 + num9;
              Canvas.SetRight((UIElement) uiPitchCurve3, length);
              Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0);
              this.xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1);
              uiPitchCurve1 = new UIPitchCurve()
              {
                VM = vm,
                Part = midiPart,
                PitchCurvePen = this._penPitchCurve
              };
            }
            uiPitchCurve1.Points.Add(this._pt);
          }
          num5 = num6;
          if (1000 <= uiPitchCurve1.Points.Count)
          {
            Point point2 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1];
            UIPitchCurve uiPitchCurve2 = uiPitchCurve1;
            point1 = uiPitchCurve1.Points[0];
            double x1 = point1.X;
            Canvas.SetLeft((UIElement) uiPitchCurve2, x1);
            Canvas.SetTop((UIElement) uiPitchCurve1, 0.0);
            UIPitchCurve uiPitchCurve3 = uiPitchCurve1;
            point1 = uiPitchCurve1.Points[0];
            double x2 = point1.X;
            point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1];
            double x3 = point1.X;
            point1 = uiPitchCurve1.Points[0];
            double x4 = point1.X;
            double num7 = x3 - x4;
            double length = x2 + num7;
            Canvas.SetRight((UIElement) uiPitchCurve3, length);
            Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0);
            this.xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1);
            uiPitchCurve1 = new UIPitchCurve()
            {
              VM = vm,
              Part = midiPart,
              PitchCurvePen = this._penPitchCurve
            };
            uiPitchCurve1.Points.Add(point2);
          }
        }
        index += num3;
      }
      if (uiPitchCurve1.Points.Count == 0)
        return;
      UIPitchCurve uiPitchCurve4 = uiPitchCurve1;
      point1 = uiPitchCurve1.Points[0];
      double x5 = point1.X;
      Canvas.SetLeft((UIElement) uiPitchCurve4, x5);
      Canvas.SetTop((UIElement) uiPitchCurve1, 0.0);
      UIPitchCurve uiPitchCurve5 = uiPitchCurve1;
      point1 = uiPitchCurve1.Points[0];
      double x6 = point1.X;
      point1 = uiPitchCurve1.Points[uiPitchCurve1.Points.Count - 1];
      double x7 = point1.X;
      point1 = uiPitchCurve1.Points[0];
      double x8 = point1.X;
      double num10 = x7 - x8;
      double length1 = x6 + num10;
      Canvas.SetRight((UIElement) uiPitchCurve5, length1);
      Canvas.SetBottom((UIElement) uiPitchCurve1, 1.0);
      this.xCanvasPitchCurve.AddElement((UIControl) uiPitchCurve1);
    }
"""
