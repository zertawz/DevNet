<template>
  <div>
    <v-row justify="end">
      <v-col cols="3">
        <v-text-field
          v-if="items.length > 1"
          v-model="search"
          color="secondary"
          append-icon="mdi-magnify"
          label="search a device..."
          single-line
          hide-details
        ></v-text-field>
      </v-col>
    </v-row>
    <v-data-table
      hide-default-footer
      class="row-pointer"
      :search="search"
      :headers="headers"
      :items="items"
      :items-per-page="100"
    >
      <template #[`item.data`]="{ item }">
        <span class="text-capitalize">
          {{ item.data.locality }} - {{ item.data.building }}
        </span>
      </template>

      <template #[`item.data.device_type`]="{ item }">
        <span v-if="item.data.device_type == 'router_switch'">
          Ethernet switch router - {{ item.data.device_model }}
        </span>
        <span v-if="item.data.device_type == 'router'">
          Router - {{ item.data.device_model }}
        </span>
      </template>
      <template #[`item.actions`]="{ item }">
        <v-tooltip bottom>
          <template #activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              icon
              color="secondary"
              v-on="on"
              @click="onView(item)"
            >
              <v-icon> mdi-magnify </v-icon>
            </v-btn>
          </template>
          <span> Detail </span>
        </v-tooltip>

        <v-tooltip bottom>
          <template #activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              icon
              color="error"
              v-on="on"
              @click="onDelete(item)"
            >
              <v-icon> mdi-delete-circle-outline </v-icon>
            </v-btn>
          </template>
          <span> Delete this device </span>
        </v-tooltip>
      </template>
      <template #no-data> No data .... </template>
      <template #no-results> No data ....</template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: null,
    },
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Hostname",
          value: "name",
          align: "center",
        },
        {
          text: "Ip address",
          value: "hostname",
          align: "center",
        },
        {
          text: "Type",
          value: "data.device_type",
          align: "center",
        },
        {
          text: "Location",
          value: "data",
          align: "center",
        },
        {
          text: "Actions",
          value: "actions",
          align: "center",
        },
      ],
    };
  },
  mounted() {},
  methods: {
    onView(item) {
      this.$emit("onAction", { item, action: "show" });
    },

    onDelete(item) {
      this.$emit("onAction", { item, action: "delete" });
    },
  },
};
</script>
<style scoped>
.row-pointer >>> tbody tr :hover {
  cursor: pointer;
}
</style>
