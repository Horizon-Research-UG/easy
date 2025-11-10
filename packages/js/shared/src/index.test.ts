import { describe, expect, it } from "vitest";

import { describeService } from "./index";

describe("describeService", () => {
  it("formats summary with description", () => {
    expect(
      describeService({ name: "backend", version: "0.1.0", description: "API layer" })
    ).toBe("backend v0.1.0 – API layer");
  });
});
