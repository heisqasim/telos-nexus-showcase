import unittest

from bms_observation import LinkState, PointSample, observe_equipment

S = PointSample(observed_at=100.0, running=True, fault_active=True)


class ObservationTests(unittest.TestCase):
    def test_connected_sample(self):
        result = observe_equipment(
            now=110, live_requested=True, transport_connected=True, sample=S
        )
        self.assertEqual(result.link, LinkState.ONLINE)
        self.assertTrue(result.running)
        self.assertTrue(result.alarm_is_current)

    def test_transport_loss_does_not_claim_equipment_stopped(self):
        result = observe_equipment(
            now=110, live_requested=True, transport_connected=False, sample=S
        )
        self.assertEqual(result.link, LinkState.NO_LINK)
        self.assertIsNone(result.running)
        self.assertTrue(result.alarm_active)
        self.assertFalse(result.alarm_is_current)

    def test_stale_does_not_reuse_running_truth(self):
        result = observe_equipment(
            now=170, live_requested=True, transport_connected=True, sample=S
        )
        self.assertEqual(result.link, LinkState.STALE)
        self.assertIsNone(result.running)
        self.assertFalse(result.alarm_is_current)

    def test_offline_is_not_process_alarm(self):
        result = observe_equipment(
            now=410, live_requested=True, transport_connected=True, sample=S
        )
        self.assertEqual(result.link, LinkState.OFFLINE)
        self.assertIsNone(result.running)
        self.assertFalse(result.alarm_is_current)

    def test_no_sample_not_assumed_healthy(self):
        result = observe_equipment(
            now=120, live_requested=True, transport_connected=True, sample=None
        )
        self.assertEqual(result.link, LinkState.OFFLINE)
        self.assertIsNone(result.alarm_active)

    def test_explicit_demo_only(self):
        result = observe_equipment(
            now=120, live_requested=False, transport_connected=False, sample=S
        )
        self.assertEqual(result.link, LinkState.DEMO)
        self.assertEqual(result.source, "DEMO")
        self.assertIsNone(result.running)

    def test_future_timestamp_rejected(self):
        with self.assertRaises(ValueError):
            observe_equipment(
                now=50, live_requested=True, transport_connected=True, sample=S
            )


if __name__ == "__main__":
    unittest.main()
