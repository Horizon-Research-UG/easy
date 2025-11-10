export interface ServiceInfo {
  name: string;
  version: string;
  description?: string;
}

export const describeService = (info: ServiceInfo): string => {
  const summary = `${info.name} v${info.version}`; // Was passiert: Basistext bauen; Wer ruft wen: describeService nutzt info; Relevanz: Serviceidentität.
  return info.description ? `${summary} – ${info.description}` : summary; // Was passiert: Beschreibung anhängen; Wer ruft wen: describeService->Ternary; Relevanz: Ausgabeformat.
};
