
from pathlib import Path
import pandas as pd

class Collector:
    def collect(self, include_seoul=True, include_incheon=True):
        input_dir=Path("input")
        frames=[]
        for f in input_dir.glob("*"):
            try:
                if f.suffix.lower()==".csv":
                    try:
                        df=pd.read_csv(f,encoding="cp949")
                    except:
                        df=pd.read_csv(f,encoding="utf-8")
                elif f.suffix.lower() in [".xlsx",".xls"]:
                    df=pd.read_excel(f)
                else:
                    continue
                addr=None
                for c in df.columns:
                    if "주소" in c or "소재지" in c:
                        addr=c
                        break
                if not addr:
                    continue
                cond=False
                if include_seoul:
                    cond=cond|df[addr].astype(str).str.startswith("서울")
                if include_incheon:
                    cond=cond|df[addr].astype(str).str.startswith("인천")
                out=df[cond].drop_duplicates()
                frames.append(out)
            except Exception:
                pass

        if not frames:
            pd.DataFrame(columns=["업체명","주소"]).to_excel("output/서울_인천_자동차정비업체.xlsx",index=False)
            return 0

        result=pd.concat(frames,ignore_index=True)
        result.to_excel("output/서울_인천_자동차정비업체.xlsx",index=False)
        return len(result)
